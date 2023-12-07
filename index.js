const express = require('express')
const connections = require('./connections.js')

const app = express()

app.get('/enterprise', async (req,res) => {
    try{
        const siret = req.query.siret
        const result = await connections.get_enterprise(siret)
        console.log(result)
        res.status(200).json(result)
    }catch(error){
        res.status(500)
        console.log(error)
    }

})

app.delete('/enterprise', async (req,res) =>  {
    try{
        const siret = req.query.siret
        const result = connections.post_enterprise(siret)
        res.status(200)
    }catch(error){
        console.log(error)
        res.status(500)
    }

})
app.post('/enterprise', async (req,res) =>  {
    try {
        const enterprise_to_add = req.query
        const result = connections.post_enterprise(enterprise_to_add)
        res.status(200)
    }catch(error){
        console.log(error)
        res.status(500)
    }


})



app.listen(8080, () => {console.log("Server is running on port 8080")})
