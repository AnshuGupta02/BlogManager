from appCP import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column (db.String(100), nullable = False)
    blog=db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable = False)

    def __repr__(self):
        return f'{self.title} bna hai {self.date} likha hai {self.blog}\n'