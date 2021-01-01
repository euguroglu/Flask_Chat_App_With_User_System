from flask import Flask, render_template
from form import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret1'

@app.route("/",methods = ['GET','POST'])
def index():

    form = RegistrationForm()
    if form.validate_on_submit():
        return "Great success!"

    return render_template('index.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
