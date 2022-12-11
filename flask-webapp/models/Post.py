from db import db


class Post(db.Model):
    #create
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    desc = db.Column(db.Text)
    author = db.Column(db.String(30))
    created_date = db.Column(db.Date)

    def __init__(self, title,desc,author,created_date):
        self.title = title
        self.desc = desc
        self.author = author
        self.created_date = created_date

    def create(post_dict):
        new_blog_post = Post(
            title = post_dict['title'],
            desc= post_dict['desc'],
            author=post_dict['author'],
            created_date = post_dict['created_date']

        )

        db.session.add(new_blog_post)
        db.session.commit()    