#!/usr/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello world! Can I get some CSS please?!'

app.run()
