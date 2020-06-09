from flask import Flask, jsonify
app=Flask(__name__)

@app.route('/', methods= ['GET'])
def hello():
    return jsonify({"about": "Hello World"})

@app.route('/blog/<int:num>/')
def get_multiply10(num):
    return jsonify({"answer": num*10})


if __name__=='__main__':
    app.run(debug=True)