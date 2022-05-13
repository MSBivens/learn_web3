from flask import render_template,redirect,session,request, flash
from flask_app import app
from flask_app.models.admin import Admin
from flask_app.models.suggestion import Suggestion
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/register',methods=['POST'])
def register():
    print(request.form)
    if not Admin.validate_register(request.form):
        return redirect('/admin')
    data ={ 
        "username": request.form['username'],
        "email": request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password'])
    }
    id = Admin.save(data)
    session['admin_id'] = id
    return redirect('/dashboard')

@app.route('/login',methods=['POST'])
def login():
    print(request.form)
    admin = Admin.get_by_email(request.form)
    if not admin:
        flash("Invalid Email","login")
        return redirect('/')
    if not bcrypt.check_password_hash(admin.password, request.form['password']):
        flash("Invalid Password","login")
        return redirect('/')
    session['admin_id'] = admin.id
    return redirect('/dashboard')

@app.route('/dashboard')
def dashboard():
    if 'admin_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['admin_id']
    }
    return render_template("admindash.html",admin=Admin.get_by_id(data),suggestions=Suggestion.get_all())

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')