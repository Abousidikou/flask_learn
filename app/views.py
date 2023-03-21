from app import app

from flask import render_template
from markupsafe import escape


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/name/<name>')
def hello(name):
    return f"Hello {escape(name)}"

@app.route('/post_id/<int:post_id>')
def post_id(post_id):
    return f"Your post ID: {escape(post_id)}"

@app.route('/about')
def about():
    return "<h1> This is about page </h1>"


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'