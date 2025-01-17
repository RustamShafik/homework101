import json
from unittest.mock import mock_open, patch

from src.utils import transactions_dict_return  # Импорт функции


def test_transactions_dict_return():
    # Поддельные данные JSON
    mock_file_data = json.dumps([{"amount": 150.0, "currency": "EUR"}])

    # Подменяем встроенную функцию open
    with patch("builtins.open", mock_open(read_data=mock_file_data)):
        # Вызываем функцию
        result = transactions_dict_return("dummy_path.json")
        # Проверяем результат
        assert result == [
            {"amount": 150.0, "currency": "EUR"}], f"Expected [{'amount': 150.0, 'currency': 'EUR'}], but got {result}"
