const path = require('path');
const fs = require('fs');

const express = require('express');
const bodyParser = require('body-parser');

const errorController = require('./controllers/error')

const app = express();
 
app.set('view engine', 'ejs');
app.set('views', 'views'); // This is already default

const adminRoutes = require('./routes/admin');
const shopRoutes = require('./routes/shop');

app.use(bodyParser.urlencoded({extended: false}));
app.use(express.static(path.join(__dirname, 'public')));  // exclude 'public' dir from public paths (i.e. in HTML page)

files = ['products.json']

for (let file of files) {
    const p = path.join(path.dirname(process.mainModule.filename), 
        'data',
        file
    );

    fs.readFile(p, (err, data) => {
        if (data.length === 0) {
            fs.writeFile(p, '[]', err => {
                if (err) {
                    console.log(err);
                }
            });
        }
    });
}

app.use('/admin', adminRoutes); // only routes with /admin will use this
app.use(shopRoutes);

app.use(errorController.get404);

app.listen(3000);