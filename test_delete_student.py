from sqlalchemy import text


class TestDeleteStudent:

    def test_delete_student_success(self, connection):
        with connection.begin():
            connection.execute(
                text(
                    "INSERT INTO students (name, age) "
                    "VALUES (:name, :age)"
                ),
                {"name": "Петр", "age": 22}
            )

        result = connection.execute(
            text("SELECT id FROM students WHERE name = :name"),
            {"name": "Петр"}
        )
        student_id = result.fetchone()[0]

        with connection.begin():
            connection.execute(
                text("DELETE FROM students WHERE id = :id"),
                {"id": student_id}
            )

        result = connection.execute(
            text("SELECT id FROM students WHERE id = :id"),
            {"id": student_id}
        )
        assert result.fetchone() is None