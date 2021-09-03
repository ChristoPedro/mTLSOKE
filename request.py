from flask import Flask
from flask import request
import os, sys
import requests

app = Flask(__name__)


def get_dados():

    result = requests.request('GET',
    'https://httpbin.poc-cloud.cf/data',
    cert=('/home/opc/cert/chaves/certificados/client.example.com.crt', '/home/opc/cert/chaves/certificados/client.example.com.key'),
    verify='/home/opc/cert/chaves/certificados/example.com.crt')
   
    return result.text

@app.route("/dados", methods=["GET"])
def response():
    
    return get_dados()

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0')
