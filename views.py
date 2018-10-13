import re

import markdown
from flask import render_template, request
from pygments.styles import get_style_by_name

from .app import app, pages

markdown_ext = ['codehilite', 'extra']


@app.route('/')
def home():
    posts = [p for p in pages if p.meta.get('layout') == 'post']

    # sort by date
    sorted_posts = sorted(posts, reverse=True, key=lambda p: p.meta.get('date'))

    return render_template('html/index.html', pages=sorted_posts)


@app.route('/search/<tag>')
def search(tag):
    def tags(p):
        return p.meta.get('tags')

    posts = [p for p in pages if tags(p) and tag in tags(p)]

    sorted_posts = sorted(posts, reverse=True, key=lambda p: p.meta.get('date'))

    return render_template('html/index.html', pages=sorted_posts)


@app.route('/query')
def search_query():
    q = request.args.get('q')
    q = re.sub(r'\s*', '', q)
    p_q = re.compile(r'\s*'.join(q), re.I)

    def match_query(p):
        title = p.meta.get('title')
        if p_q.search(title):
            return True

        # body is markdown. not html
        for m in p_q.finditer(p.body):
            if m:
                return True

        return False

    posts = [p for p in pages if match_query(p)]
    sorted_posts = sorted(posts, reverse=True, key=lambda p: p.meta.get('date'))

    return render_template('html/index.html', pages=sorted_posts)


@app.route('/<path:path>/')
def page(path):
    # path is the filename of a page, without the file extension
    post = pages.get_or_404(path)
    post.body = markdown.markdown(post.body, extensions=markdown_ext)
    return render_template('html/page.html', page=post)


@app.route('/about.html')
def me():
    return render_template('html/about.html', page=pages.get_or_404('about'))
