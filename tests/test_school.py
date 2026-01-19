import pytest

from source.school import Student, Classroom, TooManyStudents, Teacher


def test_classroom_initialization(classroom, teacher, students):
    assert classroom.teacher == teacher
    assert classroom.students == students
    assert classroom.course_title == "Math"

@pytest.mark.parametrize("initial_count", [0, 5, 10])
def test_add_student_within_limit(teacher, initial_count, students,classroom):
    new_student = Student("NewStudent")
    classroom.add_student(new_student)
    assert new_student in classroom.students

def test_add_student_too_many_students(teacher):
    students = [Student(f"S{i}") for i in range(11)]
    classroom = Classroom(teacher, students, "Chemistry")
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Overflow"))

def test_remove_existing_student(classroom, students):
    student_to_remove = classroom.students[0]
    classroom.remove_student(student_to_remove.name)
    assert student_to_remove not in classroom.students

def test_remove_non_existing_student_does_not_fail(classroom, students):
    initial_students = classroom.students.copy()
    classroom.remove_student("Ghost")
    assert classroom.students == initial_students


def test_change_teacher(classroom, teacher):
    new_teacher = Teacher("Bob")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher == new_teacher


@pytest.mark.parametrize("cls", [Student, Teacher])
def test_person_name(cls):
    person = cls("John")
    assert person.name == "John"