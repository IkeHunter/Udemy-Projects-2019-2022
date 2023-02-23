const path = require('path');

const express = require('express');
const bodyParser = require('body-parser');
// const expressHbs = require('express-handlebars')

const app = express();
 
/*
app.engine('hbs', expressHbs({
    layoutsDir: 'views/layouts/', 
    defaultLayout: 'main-layout', 
    extname: 'hbs'
}));  // This is already default

// app.set('view engine', 'pug');
*/
app.set('view engine', 'ejs');
app.set('views', 'views'); // This is already default

const adminData = require('./routes/admin');
const shopRoutes = require('./routes/shop');

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'public')));  // exclude 'public' dir from public paths (i.e. in HTML page)
 
app.use('/admin', adminData.routes); // only routes with /admin will use this
app.use(shopRoutes);

app.use((req, res, next) => {
    res.status(404).render('404', {pageTitle: 'Page Not Found'})
});

app.listen(3000);