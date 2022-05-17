from . import auth
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm,LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required

@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, 
                    lastname=form.lastname.data,
                    email = form.email.data, 
                    username = form.username.data,
                    password = form.password.data,
                    locations = form.location.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    title = "BlogApp | Sign In"
    return render_template('auth/register.html',registration_form = form, title=title)

# Login route
@auth.route("/", methods=["GET", "POST"], strict_slashes=False)
def login():
    login_form = LoginForm()
    if request.method == 'POST':
        form = request.form
        username = form.get('username')
        password = form.get('password')
        print(username)
        user = User.query.filter_by(username=username).first()
        if user is None:
            error = 'A user with that username  does not exist'
            return render_template('login.html', error=error)
        is_correct_password = user.check_password(password)
        print(is_correct_password)
        if not is_correct_password:
            error = 'A user with that password does not exist'
            return render_template('login.html', error=error)
        login_user(user)
        return redirect('/')
    return render_template('login.html', login_form = login_form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))@auth.route('/logout')
