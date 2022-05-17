from flask import (render_template, url_for, flash,
                   redirect, request, abort, Blueprint)

from App import db
from App.models import Post
from App.posts.forms import PostForm
from App.posts.utils import save_picture

posts = Blueprint('posts', __name__)

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








