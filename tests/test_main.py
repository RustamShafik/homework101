import unittest
from unittest.mock import patch
from io import StringIO
import os
import json
from src.main import main

class TestMain(unittest.TestCase):
    def setUp(self):
        # Определяем абсолютный путь к тестовому файлу
        self.test_json_path = os.path.join(os.path.dirname(__file__), "..", "data", "operations.json")

        # Создаем минимальный тестовый JSON-файл
        self.test_json_data = [
            {
                "state": "EXECUTED",
                "date": "2023-10-01T12:00:00Z",
                "description": "Payment",
                "operationAmount": {
                    "currency": {
                        "code": "RUB"
                    }
                }
            }
        ]
        os.makedirs(os.path.dirname(self.test_json_path), exist_ok=True)  # Создаем папку, если её нет
        with open(self.test_json_path, "w", encoding="utf-8") as f:
            json.dump(self.test_json_data, f)

    def tearDown(self):
        """Удаление тестового JSON-файла после тестов"""
        if os.path.exists(self.test_json_path):
            os.remove(self.test_json_path)

    @patch('builtins.input', side_effect=['5'])
    def test_invalid_menu_choice(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            self.assertIn("Некорректный выбор", fake_out.getvalue())

    @patch('builtins.input', side_effect=['1', '', 'executed', 'нет', 'нет', 'нет'])
    def test_json_loading(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            self.assertIn("Привет!", output)
            self.assertIn("Привет!", output)

    @patch('builtins.input', side_effect=['1', '', 'executed', 'нет', 'нет', 'нет'])
    def test_status_filter(self, mock_input):
        with patch('sys.stdout', new=StringIO()) as fake_out:
            main()
            output = fake_out.getvalue()
            self.assertIn("Привет!", output)
            self.assertNotIn("CANCELED", output)


if __name__ == '__main__':
    unittest.main()
