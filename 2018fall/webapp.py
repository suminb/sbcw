import os

import click
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(app)


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String)
    body = db.Column(db.String)

    def __iter__(self):
        for column in self.__table__.columns:
            yield column.name, str(getattr(self, column.name))


@app.route('/post/<int:post_id>')
def view_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(dict(post))


@app.route('/post', methods=['POST'])
def new_post():
    subject = request.form['subject']
    body = request.form['body']

    post = Post(
        subject=subject,
        body=body)

    db.session.add(post)
    db.session.commit()

    return str(post.id)


@app.route('/post/<int:post_id>', methods=['PUT'])
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    post.subject = request.form['subject']
    post.body = request.form['body']

    db.session.add(post)
    db.session.commit()

    return ''


@app.route('/post/<int:post_id>', methods=['DELETE'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)

    db.session.delete(post)
    db.session.commit()

    return str(post.id)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    debug = bool(os.environ.get('DEBUG', False))
    app.run(port=port, debug=debug)
