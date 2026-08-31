from sqlalchemy import text


class TestUpdateStudent:

    def test_update_student_success(self, connection):
        with connection.begin():
            connection.execute(
                text(
                    "INSERT INTO students (name, age) "
                    "VALUES (:name, :age)"
                ),
                {"name": "Иван", "age": 20}
            )

        result = connection.execute(
            text("SELECT id FROM students WHERE name = :name"),
            {"name": "Иван"}
        )
        student_id = result.fetchone()[0]

        with connection.begin():
            connection.execute(
                text(
                    "UPDATE students SET age = :age "
                    "WHERE id = :id"
                ),
                {"age": 21, "id": student_id}
            )

        result = connection.execute(
            text("SELECT age FROM students WHERE id = :id"),
            {"id": student_id}
        )
        age = result.fetchone()[0]
        assert age == 21

        with connection.begin():
            connection.execute(
                text("DELETE FROM students WHERE id = :id"),
                {"id": student_id}
            )