from ..models import db, Course, course_schema, courses_schema
from .dto import CourseDto, SearchCourseDto


def view_all_courses() -> list:
    courses = Course.query.all()
    serialized_courses = courses_schema.dump(courses)
    return serialized_courses


def find_course_by_name_within_dates(searched_course: SearchCourseDto) -> list:
    courses = Course.query.filter(Course.start_date >= searched_course.start_date).\
        filter(Course.end_date <= searched_course.end_date).\
        filter(Course.name == searched_course.name).all()

    serialized_courses = courses_schema.dump(courses)
    return serialized_courses


def add_new_course(course: CourseDto):
    new_course = Course(
        name=course.name,
        start_date=course.start_date.replace(microsecond=0),
        end_date=course.end_date.replace(microsecond=0),
        lectures_amount=course.lectures_amount,
    )
    db.session.add(new_course)
    db.session.commit()


def view_course_details(course_id: int):
    course = Course.query.filter_by(id=course_id).first_or_404()
    return course_schema.dump(course)


def update_course_details(course_id: int, updated_info: CourseDto):
    course = Course.query.filter_by(id=course_id).first_or_404()

    course.name = updated_info.name
    course.start_date = updated_info.start_date
    course.end_date = updated_info.end_date
    course.lectures_amount = updated_info.lectures_amount

    db.session.commit()


def delete_course_by_id(course_id: int) -> str:
    course = Course.query.filter_by(id=course_id).first_or_404()
    if course:
        db.session.delete(course)
        db.session.commit()
        return 'Course was deleted'
    return 'There is no course with such id'
