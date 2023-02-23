const fs = require('fs');

const requestHandler = (req, res) => {
    const url = req.url
    const method = req.method
    
    res.setHeader('Content-Type', 'text/html');

    if (url === '/') {
        res.write('<html>');

        res.write('<head><title>Interweb</title></head>')
        res.write('<body><h1>Welcome to the Interwebs</h1><a href="/users"><button>Users</button><a></body>')

        res.write('</html>');

        return res.end()
    }

    if (url === '/users') {
        res.write('<html>');

        res.write('<head><title>Interweb</title></head>')
        res.write('<body><h1>The Users</h1><ul><li>John Doe</li><li>Jane Doe</li></ul>')
        res.write('<form action="/new_user" method="POST"><input type="text" name="username"><button type="submit">Submit</button></form></body>')

        res.write('</html>');

        return res.end()
    }

    if (url === '/new_user' && method === 'POST') {
        const body = [];

        req.on('data', chunk => {
            body.push(chunk);
        });

        return req.on('end', () => {
            const parsedBody = Buffer.concat(body).toString();
            const username = parsedBody.split('=')[1];

            res.statusCode = 302;
            res.setHeader('Location', `/new_users/?username=${username}`);
            return res.end()
        })
    }

    if (url.includes('/new_users/?username=')) {
        let username = url.split('=')[1];
        username = username.split('+');
        let newUsername = '';
        for (item in username) {
            newUsername = newUsername + ' ' + username[item];
        }
        res.write('<html>');

        res.write('<head><title>Interweb</title></head>')
        res.write(`<body><h1>The Users</h1><ul><li>John Doe</li><li>Jane Doe</li><li>${newUsername}</li></ul>`)
        res.write('<form action="/new_user" method="POST"><input type="text" name="username"><button type="submit">Submit</button></form></body>')

        res.write('</html>');

        console.log(`New user was added: ${newUsername}`);

        return res.end()
    }
}

exports.handler = requestHandler;
