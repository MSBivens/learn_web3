from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.suggestion import Suggestion
from flask_app.models.admin import Admin
from flask_app.models.resource import Resource

@app.route('/dashboard')
def new_resource():
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":session['admin_id']
    }
    return render_template('admindash.html',admin=Admin.get_by_id(data))

@app.route('/create/resource',methods=['POST'])
def create_resource():
    if 'admin_id' not in session:
        return redirect('/logout')
    if not Resource.validate_resource(request.form):
        return redirect('/dashboard')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "link": request.form["link"],
    }
    Resource.save(data)
    return redirect('/dashboard')

@app.route('/edit/resource/<int:id>')
def edit_resource(id):
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    admin_data = {
        "id":session['admin_id']
    }
    return render_template("edit_resource.html",edit=Resource.get_one(data),admin=Admin.get_by_id(user_data))

@app.route('/update/resource',methods=['POST'])
def update_resource():
    if 'admin_id' not in session:
        return redirect('/logout')
    if not Admin.validate_resource(request.form):
        return redirect('/new/resource')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "link": request.form["link"],
        "id": request.form['id']
    }
    Resource.update(data)
    return redirect('/dashboard')

@app.route('/resource/<int:id>')
def show_resource(id):
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    admin_data = {
        "id":session['admin_id']
    }
    return render_template("resource_lists.html",resource=Resource.get_one(data),admin=Admin.get_by_id(admin_data))

@app.route('/destroy/resource/<int:id>')
def destroy_resource(id):
    if 'admin_id' not in session:
        return redirect('/logout')
    data = {
        "id":id
    }
    Resource.destroy(data)
    return redirect('/dashboard')