from flask import jsonify, abort, Blueprint
import datetime
from models import User
UsersRoutes = Blueprint('users', __name__)


@UsersRoutes.route("/users", methods=["GET"])
def get_users():
    query = User.query.all()
    users = [User.format() for user in query]
    result = {

        "success": True,
        "users": users
    }
    return jsonify(result), 200


@UsersRoutes.route("/users", methods=["POST"])
def add_users():
    try:

        new_user_data = json.loads(request.data)

        new_name = new_user_data['name']
        new_username = new_user_data['username']
        new_password = new_user_data['password']
        new_email = new_user_data['username']
        new_phone_number = new_user_data['password']
        role = 3
        date_of_joining = datetime.date

        new_user = User(
            name=new_name,
            username=new_username,

        )

        User.insert(new_user)

        user = [new_user.format()]
        results = {
            "success": True,
            "user": user
        }
        return jsonify(results), 200
    except BaseException:
        abort(422)
