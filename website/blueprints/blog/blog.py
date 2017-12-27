from flask import current_app, Blueprint, \
    render_template, request, redirect, url_for
from website.database import db
from .models import Post
import datetime

blog = Blueprint('blog', __name__,
                 url_prefix      = '/blog',
                 template_folder = 'templates',
                 static_folder   = 'static')


@blog.route('/')
def index():
    return render_template('blog.html',
                           author      = 'Robert',
                           description = 'A great site.',
                           posts = Post.query.all()
                           )

@blog.route('/post', methods=['POST'])
def post():
    content = Post(
        date     = datetime.datetime.utcnow(),
        title    = request.form['title'],
        content  = request.form['content'],
        category = 'So much fun.')
    db.session.add(content)
    db.session.commit()

    return redirect(url_for('.index'))
