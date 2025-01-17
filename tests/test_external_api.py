from src.external_api import convert_op
import unittest
from unittest.mock import patch, Mock
@patch('src.external_api.requests.request')  # Подмена метода requests.request
def test_convert_op_success(mock_request):
    # Настройка mock-объекта для успешного ответа
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"rates": {"RUB": 75.0}}  # Подделываем JSON-ответ
    mock_request.return_value = mock_response  # Возвращаем mock-ответ

    transaction = {"amount": 150.0, "currency": "EUR"}  # Входные данные
    result = convert_op(transaction)  # Вызов функции
    expected_result = 150.0 * 75.0  # Ожидаемый результат

    # Проверка
    assert result == expected_result, f"Expected {expected_result}, but got {result}"

# # Запуск теста
# if __name__ == '__main__':
#     test_convert_op_success()
#     print("test_convert_op_success passed")

