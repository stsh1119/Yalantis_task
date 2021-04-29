from ..models import db, Course, course_schema, courses_schema
from .dto import CreateCourseDto


def view_all_courses() -> list:
    courses = Course.query.all()
    serialized_courses = courses_schema.dump(courses)
    return serialized_courses


def add_new_course(course: CreateCourseDto):
    new_course = Course(
        name=course.name,
        start_date=course.start_date,
        end_date=course.end_date,
        lectures_amount=course.lectures_amount,
    )
    db.session.add(new_course)
    db.session.commit()


def view_course_details(course_id):
    course = Course.query.filter_by(id=course_id).first()
    return course_schema.dump(course)


def find_course_by_dates():
    pass


def update_course_details():
    pass


def delete_course():
    pass
