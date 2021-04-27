from flask import Blueprint, jsonify


courses = Blueprint('courses', __name__, url_prefix='/courses')


@courses.route('/all', methods=['GET'])
def index():
    return jsonify('Hello')
