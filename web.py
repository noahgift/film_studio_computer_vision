from flask import Flask
from flask import jsonify
import logging

from hellodetect import detect

app = Flask(__name__)

@app.route('/detect/<bucket>/<name>')
def detect(bucket,name):
    """Parameters"""
    
    logging.info(f"This is bucket {bucket}, name {name}")
    result = detect(bucket,name)
    return result

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)