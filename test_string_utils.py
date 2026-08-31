import pytest
from string_utils import StringUtils

utils = StringUtils()


# Тесты для метода capitalize
class TestCapitalize:
    """Позитивные тесты"""

    def test_capitalize_normal_string(self):
        """Обычная строка с маленькой буквы"""
        assert utils.capitalize("skypro") == "Skypro"

    def test_capitalize_already_capitalized(self):
        """Строка уже с заглавной буквы"""
        assert utils.capitalize("Skypro") == "Skypro"

    def test_capitalize_with_numbers(self):
        """Строка с числами"""
        assert utils.capitalize("123skypro") == "123skypro"

    def test_capitalize_with_spaces(self):
        """Строка с пробелами в начале"""
        assert utils.capitalize("  skypro") == "  skypro"

    def test_capitalize_single_letter(self):
        """Одна буква"""
        assert utils.capitalize("s") == "S"

    def test_capitalize_russian_text(self):
        """Текст на русском"""
        assert utils.capitalize("привет") == "Привет"

    """Негативные тесты"""

    def test_capitalize_empty_string(self):
        """Пустая строка"""
        assert utils.capitalize("") == ""

    def test_capitalize_none(self):
        """None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.capitalize(None)


# Тесты для метода trim
class TestTrim:
    """Позитивные тесты"""

    def test_trim_with_spaces(self):
        """Строка с пробелами в начале"""
        assert utils.trim("   skypro") == "skypro"

    def test_trim_without_spaces(self):
        """Строка без пробелов в начале"""
        assert utils.trim("skypro") == "skypro"

    def test_trim_with_one_space(self):
        """Один пробел в начале"""
        assert utils.trim(" skypro") == "skypro"

    def test_trim_with_tabs(self):
        """Строка с табуляцией в начале (обрабатывает только пробелы)"""
        assert utils.trim("\tskypro") == "\tskypro"  # табуляция не удаляется

    def test_trim_with_spaces_and_text(self):
        """Строка с пробелами в начале и внутри"""
        assert utils.trim("   sky pro") == "sky pro"

    """Негативные тесты"""

    def test_trim_empty_string(self):
        """Пустая строка"""
        assert utils.trim("") == ""

    def test_trim_only_spaces(self):
        """Строка только из пробелов"""
        assert utils.trim("   ") == ""

    def test_trim_none(self):
        """None (ожидаем ошибку)"""
        with pytest.raises(AttributeError):
            utils.trim(None)


# Тесты для метода contains
class TestContains:
    """Позитивные тесты"""

    def test_contains_true_single_char(self):
        """Символ есть в строке (один символ)"""
        assert utils.contains("SkyPro", "S") is True

    def test_contains_true_multiple_occurrences(self):
        """Символ встречается несколько раз"""
        assert utils.contains("hello", "l") is True

    def test_contains_true_word(self):
        """Подстрока (слово) есть в строке"""
        assert utils.contains("SkyPro", "Pro") is True

    def test_contains_true_with_numbers(self):
        """Поиск цифры в строке"""
        assert utils.contains("abc123", "1") is True

    def test_contains_true_russian(self):
        """Русские символы"""
        assert utils.contains("Привет мир", "и") is True

    """Негативные тесты"""

    def test_contains_false(self):
        """Символа нет в строке"""
        assert utils.contains("SkyPro", "U") is False

    def test_contains_false_partial(self):
        """Частичное совпадение"""
        assert utils.contains("SkyPro", "SkyProo") is False

    def test_contains_empty_string(self):
        """Пустая строка"""
        assert utils.contains("", "a") is False

    def test_contains_empty_symbol(self):
        """Пустой символ для поиска"""
        # В текущей реализации пустая строка вызовет ошибку index()
        with pytest.raises(ValueError):
            utils.contains("hello", "")

    def test_contains_none_string(self):
        """None в качестве строки"""
        with pytest.raises(AttributeError):
            utils.contains(None, "a")


# Тесты для метода delete_symbol
class TestDeleteSymbol:
    """Позитивные тесты"""

    def test_delete_symbol_single_char(self):
        """Удаление одного символа"""
        assert utils.delete_symbol("SkyPro", "k") == "SyPro"

    def test_delete_symbol_word(self):
        """Удаление подстроки (слова)"""
        assert utils.delete_symbol("SkyPro", "Pro") == "Sky"

    def test_delete_symbol_multiple_occurrences(self):
        """Удаление всех вхождений символа"""
        assert utils.delete_symbol("hello world", "l") == "heo word"

    def test_delete_symbol_not_exists(self):
        """Удаление символа, которого нет в строке"""
        assert utils.delete_symbol("hello", "x") == "hello"

    def test_delete_symbol_with_numbers(self):
        """Удаление цифр из строки"""
        assert utils.delete_symbol("abc123def456", "123") == "abcdef456"

    """Негативные тесты"""

    def test_delete_symbol_empty_string(self):
        """Пустая строка"""
        assert utils.delete_symbol("", "a") == ""

    def test_delete_symbol_empty_symbol(self):
        """Удаление пустого символа (строка не меняется)"""
        assert utils.delete_symbol("hello", "") == "hello"

    def test_delete_symbol_none_string(self):
        """None в качестве строки"""
        with pytest.raises(AttributeError):
            utils.delete_symbol(None, "a")

    def test_delete_symbol_none_symbol(self):
        """None в качестве символа для удаления"""
        with pytest.raises(AttributeError):
            utils.delete_symbol("hello", None)