from flask import render_template, request, redirect, url_for, flash, abort
from . import home
from .forms import PostForm,CommentForm
from ..models import Post, User, Comment
from sqlalchemy import desc
from flask_login import current_user, login_required
from .. import login_manager

    
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



@home.route('/home')
def homepage():
    title= "AreaCode --Homepage"
    postform = PostForm()
    commentform = CommentForm()
    posts = all_posts(Post.query.order_by(desc('post_created')))
    recent_posts = all_posts(Post.query.order_by(desc('post_created')).limit(5))
    return render_template('home.html', title=title, postform=postform, commentform=commentform, recent_posts=recent_posts, posts=posts)

def all_posts(posts):
    for post in posts:
        post.user = User.query.filter_by(id=post.post_by).first()
        for comment in post.post_comments:
            comment.user = User.query.filter_by(id=comment.user.id).first()
    return posts


@home.route('/profile/<int:user_id>')
@login_required
def profile(user_id):



    return render_template('profile/profile.html')

# @home.route('/user/<uname>/update/pic',methods= ['POST'])
# @login_required
# def update_pic(uname):
#     user = User.query.filter_by(username = uname).first()
#     if 'photo' in request.files:
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         db.session.commit()
#     return redirect(url_for('main.profile',uname=uname))




# @landing.route('/<int:user_id>/profile', methods=['GET', 'POST'])
# @login_required
# def profile(user_id):
#     user = User.query.filter_by(id=user_id).first()
#     if 'photo' in request.files:
#         if user.profile_pic_path:
#             user_image = f"/{user.profile_pic_path.split('/')[1]}"
#             path = os.path.abspath(os.environ.get(
#                 'UPLOADED_PHOTOS_DEST') + user_image)
#             if os.path.exists(path):
#                 os.remove(path)
#         filename = photos.save(request.files['photo'])
#         path = f'photos/{filename}'
#         user.profile_pic_path = path
#         user.save()
#         return redirect(url_for('landing.profile', user_id=user_id))
#     return render_template('profile.html', user=user)




@home.route('/updateprofile/<int:user_id>')
@login_required
def updateprofile(user_id):

    return render_template('profile/update_profile.html')
    

# about
def about():
    return render_template('about.html')



# new post view
# @login_required
# @home.route('/post/<int:user_id>/new', methods=['GET', 'POST'])
# def newpost(user_id):
#     postform = PostForm()
#     title= "New post"
#     if postform.validate_on_submit():
#         title = postform.title.data
#         body = postform.post.data
#         post = Post(author_id=user_id,title=title, post=body)
#         post.save()
#         return redirect(url_for('home.index', user_id=user_id))
#     return render_template('forms/newpost.html', title=title, postform=postform)

# @home.route('/comment/<int:post_id>/add', methods=['POST'])
# @login_required
# def add_comment(post_id):
#     commentform = CommentForm()
#     title= "Comment"
#     if commentform.validate_on_submit():
#         comment = commentform.commentbody.data
#         new_comment = Comment(comment =comment, user_id=current_user.id, post_id=post_id)
#         new_comment.save()
#         user = User.query.filter_by(id=current_user.id).first()
#         comment = {'comment':commentform.commentbody.data, 'user':user.username,
#                    'post':post_id}
#         flash("New comment added success successfully", 'success')
#         # return jsonify(comment)
#         return redirect(url_for('index.html', user_id=current_user.id))
#     return render_template('index.html', title=title)

        

