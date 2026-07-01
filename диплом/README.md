Автотесты для Кинопоиска:

Проект автоматизированного тестирования сайта [Кинопоиск](https://www.kinopoisk.ru/)
и API [PoiskKino](https://api.poiskkino.dev/v1.4).

Окружение:

-Python 3.14
-Selenium WebDriver (UI-тесты)
-Requests (API-тесты)
-pytest (запуск тестов)

Структура проекта:

-UI\UI-кейсы
-test_ui_01_search_cyrillic.py
-test_ui_02_search_and_card.py
-test_ui_03_empty_search.py
-test_ui_04_search_actor.py
-test_ui_05_random_symbols.py

-API\API-тесты
-test_api_01_get_movies.py
-test_api_02_get_movie_by_id.py
-test_api_03_invalid_id.py
-test_api_04_no_api_key.py
-test_api_05_text_in_page.py

-config.py (Настройки и тестовые данные)
-pytest.ini (Маркеры для режимов запуска)
-requirements.txt (Зависимости)
-conftest.py (Фикстуры pytest)
-README.md (Описание проекта)

Запуск тестов:
1 тип — запуск только UI-тестов:
pytest -m ui -v
(Запускаются только тесты с маркером @pytest.mark.ui)
2 тип - запуск только API-тестов:
pytest -m api -v
(Запускаются только тесты с маркером @pytest.mark.api)
3 тип — запуск всех тестов:
pytest -v

Ссылка на проект по ручному тестированию:
"https://skyproqaengennrt.yonote.ru/share/2d1bf9b3-5969-4d29-ba97-4a1a9a044065"