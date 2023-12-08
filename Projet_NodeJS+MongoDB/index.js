const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const morgan = require('morgan')
const fs = require('fs')
const connections = require('./connections.js')

var logFile = fs.createWriteStream('./myLogFile.log', {flags: 'a'});

const app = express()
app.use(bodyParser.urlencoded({extended:true}));
app.use(morgan('combined', { stream: logFile }));

app.get('/enterprise', async (req,res) => {
    try{
        const get_siret = req.query.siret
        connections.Enterprise.find({siret:parseInt(get_siret)}).then((result) => {
            console.log(result);
            res.status(200).send(result)
        }).catch((error)=>{
            console.log(error)

        })
    }catch(error){
        res.status(500)
        console.log(error)
    }
})

app.delete('/enterprise', async (req,res) => {
    try{
        const get_siret = req.query.siret
        await connections.Enterprise.deleteMany({siret: parseInt(get_siret)})
        res.status(200).send("success")
    }catch(error){
        res.status(500)
        console.log(error)
    }
})

app.post('/enterprise', async (req,res) =>  {
    try {
        const enterprise_to_add = req.body
        new_company = new connections.Enterprise(enterprise_to_add)
        await new_company.save()
        res.status(200).send("success")
    }catch(error){
        console.log(error)
        res.status(500)
    }
})

app.put('/enterprise', async (req,res) =>  {
    try{
        const enterprise_to_update = req.body
        const get_siret = enterprise_to_update.siret
        await connections.Enterprise.findOneAndUpdate({siret: parseInt(get_siret)},enterprise_to_update)
        res.status(200).send("success")
    }catch(error){
        res.status(500)
        console.log(error)
    }
})

app.listen(8080, () => {console.log("Server is running on port 8080")})
