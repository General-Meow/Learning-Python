from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage() -> str:
    return 'hello'

@app.route('/render')
def render_example() -> 'html':
    return render_template('firstPage.html', title='this is a dynamic title')

@app.route('postForm', method=['POST'])
def post_example() -> 'html':
    form_property1 = request.form['property1']
    form_property2 = request.form['property2']
    return render_example('postPage.html', property1=form_property1, property2=form_property2)

app.run(debug=True)
