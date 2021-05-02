# Yalantis_task

### How to run the project

1. Clone a project from github and create a virtual environment
2. run "pip install -r requirements.txt"
3. run "python run.py"

### Endpoints Usage

#### View all existing courses

/courses [GET]

Response example:
```JSON
[
  {
    "end_date": "2020-05-29T21:55:07",
    "id": 1,
    "lectures_amount": 15,
    "name": "test course 1",
    "start_date": "2020-04-29T21:55:07"
  },
  {
    "end_date": "2020-05-29T21:55:07",
    "id": 2,
    "lectures_amount": 15,
    "name": "test course 1",
    "start_date": "2020-04-29T21:55:07"
  }
]
```

#### View a course by id

/courses/{id} [GET]

Response example:
```JSON
{
  "end_date": "2020-05-29T21:55:07",
  "id": 2,
  "lectures_amount": 15,
  "name": "test course 1",
  "start_date": "2020-04-29T21:55:07"
}
```

#### Find a course using course name and date range:

/courses?name={course_name}&start_date={start_date}&end_date={end_date} [GET]

Example
```
/courses?name=test course 5555&start_date=2019-05-29 21:55:07&end_date=2023-08-29 21:55:07
```

Response example:
```JSON
[
  {
    "end_date": "2022-08-29T21:55:07",
    "id": 6,
    "lectures_amount": 10,
    "name": "test course 5555",
    "start_date": "2022-07-29T21:55:07"
  }
]
```

#### Add new course:

/courses/ [POST]

JSON Body example:
```json
{
	"name": "test course 5555",
	"start_date": "2022-07-29 21:55:07",
	"end_date": "2022-08-29 21:55:07",
	"lectures_amount": 10
}
```


#### Update course details:

/courses/{id} [PATCH]

JSON Body example:
```json
{
	"name": "Update for the course#3",
	"start_date": "2022-07-29 21:55:07",
	"end_date": "2022-08-29 21:55:07",
	"lectures_amount": 10
}
```

#### Delete a course:

/courses/{id} [DELETE]

Response:
```
"Course was deleted"
```