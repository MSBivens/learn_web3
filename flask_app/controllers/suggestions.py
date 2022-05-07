from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.suggestion import Suggestion
from flask_app.models.admin import Admin
from flask_app.models.resource import Resource

# How to make this from any user accessible page?
# Also make this available to anyone, no sign-in required
# Is the answser to just delete any call to admin 
# For redirect, send back to page user submitted resource from
@app.route('/new/suggestion')
def new_suggestion():
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['admin_id']
    }
    return render_template('admindash.html',admin=Admin.get_by_id(data))


@app.route('/create/suggestion',methods=['POST'])
def create_suggestion():
    if 'admin_id' not in session:
        return redirect('/logout')
    if not Suggestion.validate_suggestion(request.form):
        return redirect('/new/suggestion')
    data = {
        "title": request.form["title"],
        "link": request.form["link"],
    }
    Suggestion.save(data)
    return redirect('/dashboard')

@app.route('/destroy/suggestion/<int:id>')
def destroy_suggestion(id):
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Suggestion.destroy(data)
    return redirect('/dashboard')