import flask
from flask import Flask, jsonify, session

from model import Album

app=Flask(__name__)

@app.route("/posts")
def user():
        return  jsonify({"Title" : "ABCD"},
                        {"Title":"The Bell Jar"})


if __name__ == '__main__':
       app.run(debug=True)