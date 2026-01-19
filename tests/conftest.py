import pytest

from source import shapes
from source.school import Classroom, Student, Teacher


@pytest.fixture
def my_rectangle():
    return shapes.Rectangle(10, 20)

@pytest.fixture
def weird_rectangle():
    return shapes.Rectangle(5,6)

@pytest.fixture
def teacher():
    return Teacher("Alice")


@pytest.fixture
def students():
    return [Student(f"Student{i}") for i in range(5)]


@pytest.fixture
def classroom(teacher, students):
    return Classroom(
        teacher=teacher,
        students=students.copy(),
        course_title="Math"
    )

