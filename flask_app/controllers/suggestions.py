from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.suggestion import Suggestion
from flask_app.models.admin import Admin
from flask_app.models.resource import Resource

@app.route('/create/suggestion',methods=['POST'])
def create_suggestion():
    data = {
        "title": request.form["title"],
        "link": request.form["link"],
        "type": request.form["type"],
    }
    Suggestion.save(data)
    return redirect(request.referrer)

@app.route('/destroy/suggestion/<int:id>')
def destroy_suggestion(id):
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Suggestion.destroy(data)
    return redirect('/dashboard')