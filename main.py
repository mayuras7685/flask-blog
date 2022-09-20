from app import app
from posts.blueprint import posts


app.register_blueprint(posts, url_prefix= '/blog')
# localhost:5000/blog


if __name__ == '__main__':
  app.run()
