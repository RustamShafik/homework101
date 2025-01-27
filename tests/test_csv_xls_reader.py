import unittest
from unittest.mock import mock_open, patch
from src.csv_xls_reader import read_transactions_csv, read_transactions_xls


class TestReadTransactionsCSV(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data="""id;state;date;amount;currency_name;currency_code;from;to;description
650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации
3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту
593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту
366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 0325955596714937;Visa 3820488829287420;Перевод с карты на карту
5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада""")
    def test_read_transactions_csv(self, mock_file):
        transactions = read_transactions_csv('fake_path.csv')

        expected = [{'id;state;date;amount;currency_name;currency_code;from;to;description': '650703;EXECUTED;2023-09-05T11:30:32Z;16210;Sol;PEN;Счет 58803664561298323391;Счет 39745660563456619397;Перевод организации'}, {'id;state;date;amount;currency_name;currency_code;from;to;description': '3598919;EXECUTED;2020-12-06T23:00:58Z;29740;Peso;COP;Discover 3172601889670065;Discover 0720428384694643;Перевод с карты на карту'}, {'id;state;date;amount;currency_name;currency_code;from;to;description': '593027;CANCELED;2023-07-22T05:02:01Z;30368;Shilling;TZS;Visa 1959232722494097;Visa 6804119550473710;Перевод с карты на карту'}, {'id;state;date;amount;currency_name;currency_code;from;to;description': '366176;EXECUTED;2020-08-02T09:35:18Z;29482;Rupiah;IDR;Discover 0325955596714937;Visa 3820488829287420;Перевод с карты на карту'}, {'id;state;date;amount;currency_name;currency_code;from;to;description': '5380041;CANCELED;2021-02-01T11:54:58Z;23789;Peso;UYU;;Счет 23294994494356835683;Открытие вклада'}]

        self.assertEqual(transactions, expected)

        mock_file.assert_called_with('fake_path.csv')

    @patch('pandas.read_excel')
    def test_read_transactions_xls_with_error(self, mock_read_excel):
        mock_read_excel.side_effect = FileNotFoundError("Файл не найден")

        with self.assertRaises(FileNotFoundError):
            read_transactions_xls('fake_path.xlsx')




if __name__ == '__main__':
    unittest.main()