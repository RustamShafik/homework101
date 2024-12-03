def get_mask_card_number(card_numba: int) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    numba_str = str(card_numba)
    return f"{numba_str[0:4]} {numba_str[4:6]}** **** {numba_str[-4:]}"


def get_mask_account(account: int) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    account_str = str(account)
    return f"**{account_str[-4:]}"


print(get_mask_card_number(7000792289606361))
print(get_mask_account(73654108430135874305))
