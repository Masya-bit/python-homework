from sqlalchemy import text


class TestAddStudent:

    def test_add_student_success(self, connection):
        with connection.begin():
            connection.execute(
                text(
                    "INSERT INTO students (name, age) "
                    "VALUES (:name, :age)"
                ),
                {"name": "Максим", "age": 25}
            )

        result = connection.execute(
            text("SELECT id FROM students WHERE name = :name"),
            {"name": "Максим"}
        )
        student = result.fetchone()
        assert student is not None
        student_id = student[0]

        with connection.begin():
            connection.execute(
                text("DELETE FROM students WHERE id = :id"),
                {"id": student_id}
            )