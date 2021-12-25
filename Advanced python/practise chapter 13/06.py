# explore the flask module and create a web server using flask and python.?
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__=="__main__":
    app.run(debug=True)