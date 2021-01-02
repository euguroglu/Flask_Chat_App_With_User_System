from flask import Flask, render_template, redirect, url_for,flash
from form import *
import os
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user,current_user,login_required,logout_user

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = 'secret1'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
#configure flask login
login = LoginManager(app)
login.init_app(app)

#if we are not define database name flask will use lower case class name
#which is User(user) as table name
class User(UserMixin,db.Model):

    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(25),unique=True,nullable=False)
    password = db.Column(db.String(),nullable=False)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route("/",methods = ['GET','POST'])
def index():

    form = RegistrationForm()

    if form.validate_on_submit():

        username = form.username.data
        password = form.password.data
#Password hashing using passlib(function takes care of salt as well)
        hashed_password = pbkdf2_sha256.hash(password)

        #Add user to database
        user = User(username=username,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Registered succesfully. Please login.','success')
        return redirect(url_for('login'))

    return render_template('index.html',form=form)

@app.route('/login',methods = ['GET','POST'])
def login():

    form = LoginForm()

    #Allow login if validation success
    if form.validate_on_submit():
        user_object = User.query.filter_by(username=form.username.data).first()
        login_user(user_object)

        return redirect(url_for('chat'))

    return render_template('login.html',form=form)

@app.route('/chat',methods=['GET','POST'])
def chat():

    if not current_user.is_authenticated:
        flash('Please login.','danger')
        return redirect(url_for('login'))

    return "Chat"

@app.route('/logout',methods=['GET'])
def logout():

    logout_user()
    flash('You have logged out succesfully','success')
    return redirect(url_for('login'))


if __name__ == "__main__":
    app.run(debug=True)
