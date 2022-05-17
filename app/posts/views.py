from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from app import db
from app.models import Post
from app.posts.forms import PostForm
from app.posts.utils import save_picture

from . import posts

@posts.route("/",methods=['GET', 'POST'])
@posts.route("/post/new", methods=['GET', 'POST'])

def new_post():
    form = PostForm()
    posts = Post.query.order_by(Post.date_posted.desc())
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            image_file = picture_file
        post = Post(content=form.content.data,image_file=image_file)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('posts.new_post'))
    
    return render_template('create_post.html', title='New Post',
                           form=form,posts=posts)








