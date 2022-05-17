from flask import render_template, url_for, flash,redirect, request, abort
from flask_login import current_user, login_required
from app import db
from app.models import Post
from app.posts.forms import PostForm
from app.posts.utils import save_picture

from . import posts

@posts.route("/",methods=['GET', 'POST'])
@posts.route("/post/new", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    posts = Post.query.order_by(Post.post_created.desc())
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            image_file = picture_file
        post = Post(user_img = current_user.profile_pic,
            post_body=form.content.data,image_file=image_file, 
                    post_by=current_user.id)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.new_post'))
    
    return render_template('post/create_post.html', title='New Post',
                           form=form,posts=posts)








