### Understanding the Jinja2 templete engine
'''
{%...%}   for statement
{{   }}  Expressions to print output
(#...#)   this is for comments
'''
###Import a Flask Library:-
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

# Extract a html file:-
@app.route('/')
def Extract():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return render_template('jinja2_templete.html', result = score)

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
    
    return redirect(url_for('success', score = total_score))


if __name__ == '__main__':
    app.run(debug=True)   # debug=True is to help show all the problem on one place