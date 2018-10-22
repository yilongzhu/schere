from flask import render_template, request, redirect, url_for
from app import db
from app.proto import bp
from app.models import Post


@bp.route('/', methods=('GET', 'POST'))
@bp.route('/index', methods=('GET', 'POST'))
def index():
    if request.method == 'POST':
        post = Post(body=request.form['body'])
        db.session.add(post)
        db.session.commit()
        return redirect(url_for('proto.index'))

    posts = Post.query.all()
    return render_template('index.html', posts=posts)