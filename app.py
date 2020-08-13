from flask import Flask
import logging
from models import setup_db
app = Flask(__name__)

setup_db(app)

from routes.users import UsersRoutes
app.register_blueprint(UsersRoutes)
from routes.pharmacies import PharmaciesRoutes
app.register_blueprint(PharmaciesRoutes)
from routes.doctors import DoctorsRoutes
app.register_blueprint(DoctorsRoutes)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080)