from flask import Flask, json, jsonify, after_this_request

import models
from attendees import attendees

import os
app = Flask(__name__)

DEBUG=True

app.register_blueprint(attendees, url_prefix='/api')

@app.before_request 
def before_request():
    models.DATABASE.connect()

    @after_this_request 
    def after_request(response):
        models.DATABASE.close()
        return response 

@app.route('/')
def test():
    return 'Server connected'

if __name__ == "__main__":
    models.initialize()
    app.run(debug=DEBUG, port=5000)