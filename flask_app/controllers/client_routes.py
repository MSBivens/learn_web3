from flask import render_template
from flask_app import app
from flask_app.models.resource import Resource


@app.route('/')
def index():
    return render_template("home.html")

@app.route('/podcasts')
def podcasts():
    return render_template("podcasts.html",resources=Resource.get_all())

@app.route('/newsletters')
def newsletters():
    return render_template("newsletters.html",resources=Resource.get_all())

@app.route('/discords')
def discords():
    return render_template("discords.html",resources=Resource.get_all())

@app.route('/twitters')
def twitters():
    return render_template("twitters.html",resources=Resource.get_all())

@app.route('/4dev')
def dev():
    return render_template("4dev.html",resources=Resource.get_all())