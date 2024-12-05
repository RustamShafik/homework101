def get_mask_card_number(card_numba: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    return f"{card_numba[:-12]} {card_numba[-12:-10]}** **** {card_numba[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    return f"**{account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
