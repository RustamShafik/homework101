def log(filename=None):
    """
        Декоратор для логирования успешного выполнения функции или ошибок.

        Если указан filename, логи записываются в файл, иначе логи выводятся в консоль.
        """
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                message = f"{func.__name__} ok"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                return result
            except Exception as e:
                message = f"{func.__name__} error: {type(e).__name__}. Inputs: {args}, {kwargs}"
                if filename:
                    with open(filename, "a") as f:
                        f.write(message + "\n")
                else:
                    print(message)
                raise
        return wrapper
    return decorator
