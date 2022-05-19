from .. import db, photos
from flask import render_template,current_app, url_for, flash, abort, jsonify, request, redirect
from . import home
from .forms import PostForm, CommentForm, UpdateProfile
from app.auth.forms import RegistrationForm
from ..models import Post, User, Comment, Likes
from sqlalchemy import desc
from flask_login import current_user, login_required
from PIL import Image
import os
import secrets
from .. import db

@home.route('/home')
@login_required
def homepage():
    title = "AreaCode --Homepage"
    commentform = CommentForm()
    posts = all_posts(Post.query.order_by(desc('post_created')))
    recent_posts = all_posts(Post.query.order_by(desc('post_created')).limit(5))
    return render_template('home.html', title=title, commentform=commentform,
                           recent_posts=recent_posts, posts=posts)

def all_posts(posts):
    for post in posts:
        post.user = User.query.filter_by(id=post.post_by).first()
        for comment in post.post_comments:
            comment.user = User.query.filter_by(id=comment.user.id).first()
    return posts



@login_required
@home.route('/<int:user_id>/posts')
def posts(user_id):
    commentform = CommentForm()
    posts = Post.query.filter_by(post_by=user_id).all()
    return render_template('posts.html', posts=posts, commentform=commentform)

@home.route('/comment/<int:post_id>/add', methods=['POST'])
@login_required
def add_comment(post_id):
    commentform = CommentForm()
    title= "Comment"
    if commentform.validate_on_submit():
        new_comment = Comment(commenttext =commentform.commentbody.data, user_id=current_user.id, post_id=post_id)
        new_comment.save()
        user = User.query.filter_by(id=current_user.id).first()
        comment = {'comment':commentform.commentbody.data, 'user':user.username,
                   'post':post_id}
        flash("New comment added success successfully", 'success')
        return jsonify(comment)
        # return redirect(url_for('index.html', user_id=current_user.id))
    return render_template('index.html', title=title)

@home.route('/user/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = RegistrationForm()
    user = current_user
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file = save_profile_picture(form.profile_pic.data)
            image_file =picture_file
        user = User(profile_pic=image_file)
        
        db.session.add(user)
        db.session.commit()
        return render_template('profile/profile.html', user=user, form=form)
    return render_template('profile/profile.html', user=user, form=form)




def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/photos', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

@home.route('/user/updateprofile',methods= ['GET','POST'])
@login_required
def update_profile():
    user = current_user
    form = UpdateProfile()
    if form.validate_on_submit():
        user.bio = form.bio.data
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('home.profile'))
        
    return render_template('profile/update_profile.html',form=form)

@home.route('/user/pic',methods= ['GET','POST'])
def update_pic(user_id):
    user = User.query.filter_by(user_id=user_id).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic = path
        db.session.commit()
    return redirect(url_for('home.profile', user_id=user.user_id))
