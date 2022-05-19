
from datetime import datetime
from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin, current_user
from app import login_manager
from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin



class Crud():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True


class User(UserMixin, db.Model, Crud):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(100), nullable=False)
    lastname = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    pass_secure = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    locations = db.Column(db.String(255), nullable=False)
    user_bio = db.Column(db.String(255), nullable=True)
    profile_pic = db.Column(db.String(80), nullable=False, default=[('default.jpg'),('default.png'),('default.jpeg')])
    user_created = db.Column(db.DateTime, default=datetime.now())
    user_updated = db.Column(db.DateTime, default=datetime.now())
    post = db.relationship('Post', backref='user', lazy=True)
    comment = db.relationship('Comment', backref='user', lazy=True)

    

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)
    
    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

   
    def add_comment(self, comment):
        self.comments.append(comment)
        return self.save()

    def add_post(self, post):
        self.posts.append(post)
        return self.save()
     
    def __repr__(self):
        return f'User {self.username}'
        

class Post(db.Model, Crud):
    __tablename__ = 'post'

    id = db.Column(db.Integer, primary_key=True)
    user_img = db.Column(db.String(80), nullable=True)
    post_body = db.Column(db.String(200), nullable=False)
    post_created = db.Column(db.DateTime, default=datetime.now())
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
    post_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)
    post_likes = db.relationship('Likes', backref='post', lazy=True)
    post_comments = db.relationship('Comment', backref='post', lazy=True)
    
    def delete(self):
        user = User.query.filter_by(id=self.author).first()
        user.posts.remove(self)
        self.delete()
        return self.save()
   

class Comment(db.Model, Crud):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True)
    commenttext = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def delete(self):
        post = Post.query.filter_by(id=self.post).first()
        post.comments.remove(self)
        self.delete()
        return self.save()

    # def update(self):
    #     comment = Comment.query.filter_by(id=self.id).first()
    #     comment.comment = self.comment
    #     return comment.save()


class Images(db.Model, Crud):
    __tablename__ = 'images'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    uploader_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
class Likes(db.Model, Crud):
    __tablename__ = 'likes'

    id = db.Column(db.Integer, primary_key=True)
    likes = db.Column(db.Integer,default=1)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    
    def like(self, post_id):
        post_like = Likes(user=current_user, post_id=post_id)
        post_like.save()
        
    @classmethod
    def get_like(cls, id):
        like = Likes.query.filter_by(post_id=id).all()
        return like
    
    @classmethod
    def all_likes(cls):
        likes = Likes.query.order_by('post_id').all()
        return likes
    
    
    
    # def toggleLike(self):
    #     like = Likes.query.filter_by(
    #         post_id=self.post_id, user_id=self.user_id).first()
    #     if like is None:
    #         self.save()
    #     elif like:
    #         like.delete()
    #     return True

