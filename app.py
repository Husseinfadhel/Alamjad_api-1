from flask import Flask
import logging
from models import setup_db

def create_app(test_config=None):
    app = Flask(__name__)

    setup_db(app)

    from routes.salesmen import SalesmenRoutes
    app.register_blueprint(SalesmenRoutes)
    from routes.pharmacies import PharmaciesRoutes
    app.register_blueprint(PharmaciesRoutes)
    from routes.doctors import DoctorsRoutes
    app.register_blueprint(DoctorsRoutes)
    
    return app


if __name__ == '__main__':
    create_app().run(host='127.0.0.1', port=8080)