from datetime import datetime
from time import time

import re

from app import db


def slugify(s):
  pattern = r'[^\w+]'
  return re.sub(pattern, '-', s)


class Post(db.Model):
  id = db.Column(db.Integer, primary_key = True)
  title = db.Column(db.String(140))
  slug = db.Column(db.String(140), unique = True)
  body = db.Column(db.Text)
  created = db.Column(db.DateTime, default = datetime.now())


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