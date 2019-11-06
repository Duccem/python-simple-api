from flask import Flask, jsonify, request

app = Flask(__name__)

from product import products

@app.route('/')
def getProducts():
    return jsonify({"products": products})

@app.route('/<string:id>')
def getProduct(id):
    productFound = [product for product in products if product['id'] == id]
    if (len(productFound) > 0):
        return jsonify({"product":productFound[0]})
    return jsonify({"message":"Product not found"})

@app.route('/',methods=['POST'])
def addPorduct():
    newProduct = {
        "name": request.json['name'],
        "price" : request.json['price'],
        "quantity": request.json['quantity']
    }
    products.append(newProduct)
    return jsonify({"message":"Product added successfuly"})

@app.route('/<string:id>',methods=['PUT'])
def editProduct(id):
    productFound = [product for product in products if product['id'] == id]
    if(len(productFound) > 0):
        productFound[0]['name'] = request.json['name']
        productFound[0]['price'] = request.json['price']
        productFound[0]['quantity'] = request.json['quantity']
        return jsonify({"message":"Product updated"})
    return jsonify({"message":"Product not found"})

@app.route('/<string:id>',methods=['DELETE'])
def deleteProduct(id):
    productFound = [product for product in products if product['id'] == id]
    if(len(productFound) > 0):
        products.remove(productFound[0])
        return jsonify({"message":"Product deleted"})
    return jsonify({"message": "Product not found"})

if __name__ == "__main__":
    app.run(debug=True,port=4000)