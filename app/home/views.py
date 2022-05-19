from flask import render_template,current_app, url_for, flash, abort, jsonify, redirect
from . import home
from .forms import PostForm, CommentForm
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

@home.route('/<int:user_id>/profile', methods=['GET', 'POST'])
@login_required
def profile(user_id):
    form = RegistrationForm()
    users = User.query.filter_by(id=user_id).first()
    if form.validate_on_submit():
        if form.profile_pic.data:
            picture_file = save_profile_picture(form.profile_pic.data)
            image_file =picture_file
        user = User(profile_pic=image_file)
        
        db.session.add(user)
        db.session.commit()
        return render_template('profile/profile.html', user=user, form=form)
    return render_template('profile/profile.html', users=users, form=form)




def save_profile_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/photos', picture_fn)
    form_picture.save(picture_path)
    return picture_fn
    
    
# Add like to post
# @login_required
# @home.route('/post/<string:like>/<int:post_id>', methods=['POST'])
# def toggleLikes(like, post_id):
#     new_like = Likes(user_id=current_user.id, post_id=post_id)
#     new_like.toggleLike()

#     likes = Likes.query.filter_by(post_id=post_id).count()
#     return jsonify(likes)

@home.route('/like/<int:post_id>', methods=['POST', 'GET'])
@login_required
def like(post_id):
    post=Post.query.get(post_id)
    new_like = Likes(post=post,like=1, user_id=current_user.id)
    new_like.save()
    return redirect(url_for('home.homepage'))