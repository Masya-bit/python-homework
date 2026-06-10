
Название: Добавление нового студента в таблицу "students"
Тип: Позитивный
Метод: INSERT
Шаги:
1 - Выполнить INSERT: INSERT INTO students (name, age) VALUES ('Максим', 25)
ОР: Запись добавлена, коммит успешен
2 - Выполнить SELECT: SELECT id FROM students WHERE name = 'Максим'
ОР: Запрос возвращает одну строку с id, id не равен None
3 - Выполнить DELETE: DELETE FROM students WHERE id = полученный_id
ОР: Запись удалена, коммит успешен