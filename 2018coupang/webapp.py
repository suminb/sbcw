from datetime import datetime

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///webapp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Post(db.Model):

    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime)
    subject = db.Column(db.String)
    body = db.Column(db.String)

    def __iter__(self):
        for key in ['id', 'subject', 'body']:
            yield key, getattr(self, key)
        # yield 'subject', self.subject
        # yield ('body', self.body)


@app.route('/')
def index():
    context = {
        'title': 'This is a title from context',
        'content': 'This is body',
    }
    return render_template('index.html', **context)


@app.route('/posts/<post_id>')
def read_post(post_id):
    post = Post.query.get_or_404(post_id)
    return jsonify(dict(post))
    # return jsonify({
    #     'subject': post.subject,
    #     'body': post.body,
    # })


@app.route('/posts', methods=['POST'])
def new_post():
    subject = request.form['subject']
    body = request.form['body']

    post = Post(
        created_at=datetime.now(),
        subject=subject,
        body=body,
    )
    db.session.add(post)
    db.session.commit()

    return jsonify(dict(post))


@app.route('/posts/<post_id>', methods=['DELETE'])
def delete_post(post_id):
    # updated = Post.query.filter(Post.id == post_id).delete()
    # db.session.commit()
    # return str(updated)

    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()

    return str(post.id)


@app.route('/test', methods=['TROYE'])
def troye():
    param = request.form['param']
    return f'param={param}'


if __name__ == '__main__':
    app.run(port=8000, debug=True)
    # db.create_all()
