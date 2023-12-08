# Application-of-big-data-project

--------------------------------- By Alexis Locatelli & Briac Marchandise ----------------------------------------

We choose the first subject, which the purpose is to create a database and ingest data and then to create an API to communicate with it. This project was rather new for us so we had a lot of difficulty so we've done a lot of trial and error. At the end, we used two different approaches to see the difference in time ingestion and time response for each project and compare it. All the difficulty lay in the ingestion of data because the csv file we’ve provided was approximately 5,5 GB (34 billions of lines for 43 columns). Then we had to deal with Big Data problematic.  

 

Solution 1 :  

FastAPI is a Python framework and set of tools that allow developers to invoke commonly used functions using a REST interface.  

SQLAlchemy is a package that makes it easier for Python programs to communicate with databases. Most of the time, this library is used as an Object Relational Mapper (ORM) tool, which automatically converts function calls to SQL queries and translates Python classes to tables on relational databases.  

Many web, mobile, geospatial, and analytics applications use PostgreSQL as their primary data storage or data warehouse. 

 

Solution 2:  

Why did we choose this ? 

MongoDB is built on a scale-out architecture that has become popular with developers of all kinds for developing scalable applications with evolving data schemas. It have a nodeJS framework : mongoose.  

Express is a minimal and flexible Node.js web application framework that provides a robust set of features for web and mobile applications. 

Morgan is a middleware at the HTTP request level. This is a great tool that logs requests as well as other information depending on its configuration and the preset used. This is very useful when debugging and if you want to create log files. 

 

How to install it ?  

Requirement: MongoDB compass / NodeJS 

To install the project, you should open mongoDB compass on local port 27017 and create a database named “Enterprise” and a collection named “enterpises”. In the next step you need to download the datas.csv file in teams and add them to the collection using the “import data from csv” button of MongoDB compass. Then, you should download the project and put it in the choosen folder, then open cmd in the project folder: “Projet_NodeJS+MongoDB” and run the command: 

npm install –dev 

node index.js 