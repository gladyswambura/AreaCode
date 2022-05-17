<<<<<<< HEAD
from flask import render_template
from . import auth
from flask import render_template,redirect,url_for,flash,request
from ..models import User
from .forms import RegistrationForm
from .. import db
from flask_login import login_user, logout_user, login_required


@auth.route('/register',methods = ["GET","POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data,password = form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))
    
    title = "BlogApp | Sign In"
    return render_template('auth/register.html',registration_form = form, title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
=======
from flask import (render_template, redirect, request)
from flask_login import login_user
from . import auth
from ..models import User
from .forms import  LoginForm

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
>>>>>>> cbdd7d94a3e6113c55013b9e886dd7e6a60d59fc
