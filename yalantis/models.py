from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()


class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    start_date = db.Column(db.DateTime())
    end_date = db.Column(db.DateTime())
    lectures_amount = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Course('{self.id}', '{self.name}', '{self.start_date}', '{self.end_date}', '{self.lectures_amount}')"


class CourseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Course
    id = ma.auto_field()
    name = ma.auto_field()
    start_date = ma.auto_field()
    end_date = ma.auto_field()
    lectures_amount = ma.auto_field()


courses_schema = CourseSchema(many=True)
course_schema = CourseSchema()
