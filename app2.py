# Building URL Dynamically:-
# Variable Rules and URL Building:-

from flask import Flask, redirect, url_for

# Object of the flask cakkked app = Flask(__name__)
app = Flask(__name__)

# Create a Decorator:-
@app.route('/')
def Welcome():
    return "Hello World! I am a One of the best data Scientist!"

# Create a Decorator:-
# Building URL Dynamically:-
# Variable Rules and URL Building:-
@app.route('/success/<int:score>')
def success(score):
    return "Tha person has passed and his/him mark is : " + str(score)  # Here is use the concanate str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "Tha person has fail and his/him mark is : " + str(score)

### Create Result Checker
@app.route('/results/<int:marks>')
def results(marks):
    result = ""
    if marks < 40:
        result = "fail"
    else:
        result = "success"
    return redirect(url_for(result, score=marks))
    
if __name__ == '__main__':
    app.run(debug=True)