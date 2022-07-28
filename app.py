from flask import Flask
import sys

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    return 'Hello world'
    
if __name__ == "__main__":
    app.run()