from flask import Blueprint,render_template,request,flash,redirect,url_for
from .models import User
from . import db
from werkzeug.security import generate_password_hash,check_password_hash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!',category='success')
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password or email,try again.', category='error')
        else:
            flash('Email does not exist,',category='error')
    return render_template('login.html')

@auth.route('/logout')
def logout():
    return "login"

@auth.route('/sign-up',methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        fname = request.form.get('fname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(password1) < 7:
            flash('Must be greater then 7 character :(', category='error')
        elif password1 != password2:
            flash('Password don\'t match :(', category='error')        
        else :
            # add user to database 
            new_user = User(email=email,first_name=fname,password=generate_password_hash(password1,method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            flash('Account created', category='success')
            return redirect(url_for('views.home'))




    return render_template('signup.html')