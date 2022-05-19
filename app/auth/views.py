from . import auth
from flask import render_template, redirect, url_for, flash, request
from ..models import User,Images
from .forms import RegistrationForm, LoginForm
from .. import db
from flask_login import login_user, logout_user, login_required, current_user
import os
from werkzeug.utils import secure_filename

@auth.route('/register', methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data,
                    lastname=form.lastname.data,
                    email=form.email.data,
                    username=form.username.data,
                    profile_pic=form.profile_pic.data,
                    password=form.password.data,
                    locations=form.location.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    title = "BlogApp | Sign In"
    return render_template('auth/register.html', registration_form=form, title=title)

@auth.route('/user/picimage', methods=["GET", "POST"])
@login_required
def user_pic():
    user = current_user
    form = RegistrationForm()
    if form.validate_on_submit():
        file = request.files['profile_pic']
        file.save(os.path.join(os.environ.get("UPLOAD_FOLDER"),secure_filename(file.filename)))
        upload = Images(name=secure_filename(file.filename), uploader_id=current_user.id)
        upload.save()
        return redirect(url_for('auth.login'))
    return render_template("profile/update_profile.html",form=form,user=user.username)




# Login route
@auth.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get("next") or url_for("home.homepage"))
    title = "Login"
    return render_template("auth/login.html", login_form = login_form, title = title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
