from flask import render_template, url_for, flash,redirect, request, abort, Blueprint
from flask_login import login_required, current_user
from app import db
from app.models import Post
from app.posts.forms import PostForm
from app.posts.utils import save_picture
from . import posts


@posts.route("/post/new", methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    posts = Post.query.order_by(Post.post_created.desc())
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            image_file = picture_file
        post = Post(post_body=form.content.data, image_file=image_file)
        print(current_user)
        
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home.homepage'))

    return render_template('post/create_post.html', title='New Post',
                           form=form, posts=posts)
