from flask import Flask, render_template
from form import *
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'secret1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#if we are not define database name flask will use lower case class name
#which is User(user) as table name
class User(db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25),unique=True,nullable=False)
    password = db.Column(db.String(),nullable=False)


@app.route("/",methods = ['GET','POST'])
def index():

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data

        #check username exist
        user_object = User.query.filter_by(username=username).first()
        if user_object:
            return "Someone else has taken this username!"
        #Add user to database
        user = User(username=username,password=password)
        db.session.add(user)
        db.session.commit()

        return "Data Inserted to DB"

    return render_template('index.html',form=form)

if __name__ == "__main__":
    app.run(debug=True)
