import pytest
from src.processing import filter_by_state, sort_by_date
from datetime import datetime

def test_filter_by_state():
    dict_list = [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-12-02T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-03T10:00:00"}
    ]

    # Тест на фильтрацию по умолчанию (EXECUTED)
    result = filter_by_state(dict_list)
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-03T10:00:00"}
    ]
    assert result == expected

    # Тест на фильтрацию по другому состоянию
    result = filter_by_state(dict_list, state="PENDING")
    expected = [
        {"id": 2, "state": "PENDING", "date": "2023-12-02T10:00:00"}
    ]
    assert result == expected

    # Тест на отсутствие совпадений
    result = filter_by_state(dict_list, state="CANCELLED")
    assert result == []

def test_sort_by_date():
    dict_list = [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-12-03T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-02T10:00:00"}
    ]

    # Тест на сортировку по убыванию (по умолчанию)
    result = sort_by_date(dict_list)
    expected = [
        {"id": 2, "state": "PENDING", "date": "2023-12-03T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-02T10:00:00"},
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"}
    ]
    assert result == expected

    # Тест на сортировку по возрастанию
    result = sort_by_date(dict_list, order=False)
    expected = [
        {"id": 1, "state": "EXECUTED", "date": "2023-12-01T10:00:00"},
        {"id": 3, "state": "EXECUTED", "date": "2023-12-02T10:00:00"},
        {"id": 2, "state": "PENDING", "date": "2023-12-03T10:00:00"}
    ]
    assert result == expected

    # Тест на пустой список
    result = sort_by_date([])
    assert result == []

if __name__ == "__main__":
    pytest.main()