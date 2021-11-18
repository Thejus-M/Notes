from flask import Blueprint,render_template,request,flash

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    data = request.form
    print(data)
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

        if len(password1) > 7:
            flash('Must be greater then 7 character :(', category='error')
        elif password1 != password2:
            flash('Password don\'t match :(', category='error')        
        else :
            # add user to database 
            flash('Account created', category='success')

    return render_template('signup.html')