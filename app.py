from flask import Flask

app = Flask(__name__)

@app.route('/')
def members():
    return "You are bad Boy!"

@app.route('/')
def device():
    return "You are bad Boy!"
        
if __name__ == '__main__':
    app.run(debug=True)