# Integrate HTML with flask:-
## Http verb GET and POST
# Building URL Dynamically:-
# Variable Rules and URL Building:-

from flask import Flask, redirect, url_for, render_template, request

# Object of the flask cakkked app = Flask(__name__)
app = Flask(__name__)

# Create a Decorator:-
## Here is used the Jinja2 render_templetes so,
@app.route('/')
def Welcome():
    return render_template('index.html')

# Create a Decorator:-
# Building URL Dynamically:-
# Variable Rules and URL Building:-
@app.route('/success/<int:score>')
def success(score):
    res = ""
    if score >= 40:
        res =  "Pass"
    else:
        res =  "Fail"
        
    return render_template('result.html', result = res)


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

@app.route('/submit', methods = ['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        data_science = float(request.form['datascience'])
        total_score = (science + maths + c + data_science)/4
        
    res = ""
    #if total_score >= 40:
       # res = "success"
   # else:
       # res = "fail"
    
    return redirect(url_for('success', score = total_score))
    
if __name__ == '__main__':
    app.run(debug=True)