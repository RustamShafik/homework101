import pytest
from src.decorators import log


def test_log_to_console_success(capsys):
    @log()
    def add(a, b):
        return a + b

    result = add(3, 4)
    assert result == 7

    captured = capsys.readouterr()
    assert "add ok" in captured.out


def test_log_to_console_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(3, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Inputs: (3, 0), {}" in captured.out


def test_log_to_file_success(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def multiply(a, b):
        return a * b

    result = multiply(2, 5)
    assert result == 10

    with open(log_file, "r") as f:
        content = f.read()
    assert "multiply ok" in content


def test_log_to_file_error(tmp_path):
    log_file = tmp_path / "log.txt"

    @log(filename=log_file)
    def subtract(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        subtract(3, 0)

    with open(log_file, "r") as f:
        content = f.read()
    assert "subtract error: ZeroDivisionError. Inputs: (3, 0), {}" in content
