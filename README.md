# python-homework

## Запуск теста, для формирования отчета
- Для формирования Allure-отчёта используется команда "--alluredir"
- pytest tests/test_slow_calculator.py --alluredir=allure-results

## Просмотр отчета
- После того как тесты выполнены и результаты сохранены в папку allure-results, отчёт можно просмотреть двумя способами.
1 - Формирует отчёт и сразу открывает его в браузере. "allure serve allure-results". После закрытия браузера временный отчёт удаляется.
2 - Сгенерировать HTML-отчёт в папку allure-report. "allure generate allure-results -o allure-report"
  - Открыть отчёт в браузере. "allure open allure-report" Отчёт остаётся на диске, его можно открывать повторно
