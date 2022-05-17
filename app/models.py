from . import db
from datetime import datetime


class Crud():
    def save(self):
        db.session.add(self)
        db.session.commit()
        return True
        
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return True

class User(db.Model, Crud):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    profile_pic = db.Column(db.String(80), nullable=False)
    post = db.relationship('Post', backref='user', lazy=True)

class Post(db.Model, Crud):
    __tablename__ = 'post'

    
    id = db.Column(db.Integer, primary_key=True)
    user_img = db.Column(db.String(80), nullable=False)
    post_body = db.Column(db.String(200), nullable=False)
    post_likes = db.relationship('Likes', backref='post', lazy=True)
    post_comments = db.relationship('Comment', backref='post', lazy=True)
    posted_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    

class Comment(db.Model, Crud):
    __tablename__ = 'comment'

    
    id = db.Column(db.Integer, primary_key=True)
    commenttext = db.Column(db.String(200), nullable=False)
    created_at = db.Column(db.DateTime,default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'),nullable=False)
    
    def delete(self):
        post =Post.query.filter_by(id=self.post).first()
        post.comments.remove(self)
        self.delete()
        return self.save()
    
    def update(self):
        comment = Comment.query.filter_by(id=self.id).first()
        comment.comment = self.comment
        return comment.save()
    
    
class Likes(db.Model, Crud):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))