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
