const fs = require('fs');

const requestHandler = (req, res) => {

    const url = req.url;
    const method = req.method;

    if (url === '/') {
        res.write('<html>');
        res.write('<head><title>Enter Message</title><head>');
        res.write('<body><form action="/message" method="POST"><input type="text" name="message"><button type="submit">Send</button></form></body>')
        res.write('</html>');
        return res.end();
    }
    if (url === '/message' && method === 'POST') {
        const body = [];
        req.on('data', (chunk) => {  // event listener to listen to data stream
            console.log(chunk)
            body.push(chunk);
        });
        return req.on('end', () => {  // runs when the data stream stops
            const parsedBody = Buffer.concat(body).toString();
            const message = parsedBody.split('=')[1];
            fs.writeFile('message.text', message, err => {
                res.statusCode = 302;
                res.setHeader('Location', '/');
                return res.end();
            });  // writeFileSync is syncronous            
        });    
    }
    res.setHeader('Content-Type', 'text/html');
    
    res.write('<html>');
    res.write('<head><title>My Page</title><head>');
    res.write('<body><h1>This is my cool page!</h1></body>')
    res.write('</html>');
    res.end();
};

// module.exports = {
//     handler: requestHandler,
//     someText: 'hard coded text'
// };  // makes requestHandler global (in this directory)

exports.handler = requestHandler;
exports.someText = 'hard coded text';
