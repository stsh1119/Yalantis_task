from flask import Blueprint, jsonify, request
from pydantic import ValidationError
from .service import view_all_courses, add_new_course, view_course_details, delete_course_by_id, update_course_details
from .dto import CourseDto
from ..utils import json_body_required


courses = Blueprint('courses', __name__, url_prefix='/courses')


@courses.route('/', methods=['GET'])
def all_courses():
    return jsonify(view_all_courses()), 200


@courses.route('/', methods=['POST'])
@json_body_required
def add_new():
    try:
        course = CourseDto.parse_obj(request.json)
        add_new_course(course)
        return jsonify('Course was added'), 201

    except ValidationError as e:
        return e.json(), 400


@courses.route('/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    return jsonify(delete_course_by_id(course_id)), 200


@courses.route('/<int:course_id>', methods=['PATCH'])
@json_body_required
def update(course_id):
    try:
        updated_course_data = CourseDto.parse_obj(request.json)
        update_course_details(course_id, updated_course_data)
        return jsonify('Course was updated'), 200

    except ValidationError as e:
        return e.json(), 400


@courses.route('/<int:course_id>', methods=['GET'])
def view_course(course_id):
    return view_course_details(course_id), 200
