from datetime import datetime
from time import time

import re
from flask_security import UserMixin, RoleMixin
from app import db


def slugify(s):
  pattern = r'[^\w+]'
  return re.sub(pattern, '-', s)

posts_tags = db.Table('posts_tags',
                      db.Column('post_id', db.Integer,
                      db.ForeignKey('post.id')),
                      db.Column('tag_id', db.Integer,
                      db.ForeignKey('tag.id'))   
                      )

roles_users = db.Table('roles_users',
                        db.Column('user_id', db.Integer,
                        db.ForeignKey('user.id')),
                        db.Column('role_id', db.Integer,
                        db.ForeignKey('role.id'))
)


class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(140))
  slug = db.Column(db.String(140), unique = True)
  body = db.Column(db.Text)
  created = db.Column(db.DateTime, default = datetime.now())
  tags = db.relationship('Tag', secondary = posts_tags, backref=db.backref('posts'), lazy='dynamic')

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.generate_slug()

  def generate_slug(self):
    if self.title:
      self.slug = slugify(self.title)
    else:
      self.slug = str(int(time()))

  def __repr__(self):
    return f'<Post id: {self.id}, title:{self.title}>'


class Tag(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(140))
  slug = db.Column(db.String(140), unique = True)
  
  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.slug = self.generate_slug()


  def generate_slug(self):
    if self.title:
      self.slug = slugify(self.title)
    else:
      self.slug = str(int(time()))


  def __repr__(self):
    return f'<Tag id: {self.id}, title:{self.title}>'


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(100), unique=True)
  password = db.Column(db.String(255))
  active = db.Column(db.Boolean)
  roles = db.relationship('Role', secondary=roles_users,
  backref=db.backref('users'), lazy='dynamic')


class Role(db.Model, RoleMixin):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), unique=True)
