const express = require('express');
const bodyParser = require('body-parser');

const router = express.Router();

const usernames = [];

router.get('/', (req, res, next) => {
    res.render('home.ejs', {users: usernames});
});

router.get('/users', (req, res, next) => {
    res.render('users.ejs');
});

router.post('/users', (req, res, next) => {
    console.log(req.body.username)
    usernames.push({ name: req.body.username });
    res.redirect('/');
})

exports.mainRouter = router;
exports.usernames = usernames;
