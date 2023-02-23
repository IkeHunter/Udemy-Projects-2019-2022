 const express = require('express');
 const bodyParser = require('body-parser');

 const app = express();

 app.set('view engine', 'ejs');
 app.use(bodyParser.urlencoded({extended: false}))

 const mainRoutes = require('./routes/main.js');
 app.use(mainRoutes.mainRouter);

 app.listen(3000);