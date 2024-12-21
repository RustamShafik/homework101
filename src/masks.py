def get_mask_card_number(card_numba: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    if card_numba is None:
        raise ValueError("Отсутствует номер карты")
    if len(card_numba) != 16:
        raise ValueError("Номер карты должен содержать 16 символов")
    return f"{card_numba[:-12]} {card_numba[-12:-10]}** **** {card_numba[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    if type(account) != str:
        raise ValueError("Номер счета должен представлять собой строку")
    if len(account) < 4:
        raise ValueError("Номер счета должен содержать минимум 4 символа")
    return f"**{account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
