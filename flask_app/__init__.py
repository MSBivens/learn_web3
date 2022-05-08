from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/podcasts')
def podcasts():
    return render_template("podcasts.html")

@app.route('/newsletters')
def newsletters():
    return render_template("newsletters.html")

@app.route('/discords')
def discords():
    return render_template("discords.html")

@app.route('/twitters')
def twitters():
    return render_template("twitters.html")

@app.route('/4dev')
def dev():
    return render_template("4dev.html")

app.secret_key = "Get Ready to Rumble!"