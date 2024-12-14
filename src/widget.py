from masks import get_mask_account, get_mask_card_number


def mask_account_card(account: str) -> str:
    """Функция маскирует номер счета или карты"""
    if account[0:4] == "Счет":
        return f"Счет {get_mask_account(account)}"
    return get_mask_card_number(account)


def get_date(date: str) -> str:
    """Функция принимает на вход строку и форматирвует ее по условиям"""
    return f"{date[8:10]}.{date[5:7]}.{date[0:4]}"


if __name__ == "__main__":
    print(mask_account_card("Visa Platinum 7000792289606361"))
    print(mask_account_card("Maestro 7000792289606361"))
    print(mask_account_card("Счет 73654108430135874305"))
    print(get_date("2024-03-11T02:26:18.671407"))
