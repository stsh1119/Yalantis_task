from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from .service import view_all_courses, add_new_course, view_course_details
from .dto import CreateCourseDto
from ..utils import json_body_required


courses = Blueprint('courses', __name__, url_prefix='/courses')


@courses.route('/all', methods=['GET'])
def all_courses():
    return jsonify(view_all_courses()), 200


@courses.route('/new', methods=['POST'])
@json_body_required
def add_new():
    try:
        course = CreateCourseDto.parse_obj(request.json)
        add_new_course(course)
        return jsonify('Course was added'), 201

    except ValidationError as e:
        return e.json(), 400

    except Exception as e:
        return jsonify(str(e)), 400


@courses.route('/<int:course_id>', methods=['GET'])
def view_course(course_id):
    return view_course_details(course_id), 200
