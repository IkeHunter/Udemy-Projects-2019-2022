const fs = require('fs');
const path = require('path');

const Cart = require('./cart');

const p = path.join(path.dirname(process.mainModule.filename), 
    'data',
    'products.json'
);

const getProductsFromFile = (cb) => {
    
    fs.readFile(p, (err, fileContent) => {
        if (err) {
            return cb([]);
        } else {
            cb(JSON.parse(fileContent));
        }
        
    });
}

module.exports = class Product {
    constructor(id, title, imageUrl, description, price) {  // equivalent to __init__()
        this.id = id
        this.title = title;
        this.imageUrl = imageUrl;
        this.description = description;
        this.price = price;
        this.initializeDataFile;
    }

    save() {
        
        
        getProductsFromFile(products => {  // use of arrow fn ensures 'this' never loses context
            if (this.id) {
                const existingProductIndex = products.findIndex(prod => prod.id === this.id);
                const updatedProducts = [...products];
                updatedProducts[existingProductIndex] = this;
                fs.writeFile(p, JSON.stringify(updatedProducts), (err) => {
                    console.log(err);
                });
            } else {
                this.id = Math.random().toString();
                products.push(this)  // pushes the object created by the class to array
                fs.writeFile(p, JSON.stringify(products), (err) => {
                    console.log(err);
                });
            };
            
        });
    }

    static deleteById(id) {
        getProductsFromFile(products => {
            const product = products.find(prod => prod.id === id);
            const updatedProducts = products.filter(p => p.id !== id);
            
            fs.writeFile(p, JSON.stringify(updatedProducts), err => {
                if (!err) {
                    Cart.deleteProduct(id);
                }
            })
        });
    }

    static fetchAll(cb) {  // can call this function directly on class itself and not on instantiated object
        getProductsFromFile(cb);
    }

    static findById(id, cb) {
        getProductsFromFile(products => {
            const product = products.find(p => p.id === id);  // filters through all products and finds the product whose id is the param
            cb(product);
        });
    } 

};