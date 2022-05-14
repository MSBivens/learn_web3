from flask_app import app
from flask_app.controllers import admins, resources, suggestions, client_routes

if __name__=="__main__":
    app.run(debug=True)