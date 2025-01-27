import logging

logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('C:\\Users\\shafi\\PycharmProjects\\Homework10\\logs\\masks.log', mode='w')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_numba: str) -> str:
    """Функция принимает на вход номер карты и возвращает ее маску"""
    logger.debug(f'Запуск обработки номера карты {card_numba}')
    if card_numba is None:
        logger.error('Отсутствует номер карты')
        raise ValueError("Отсутствует номер карты")
    if len(card_numba) != 16:
        logger.error(f'Номер карты содержит всего {len(card_numba)} симв.')
        raise ValueError("Номер карты должен содержать 16 символов")
    return f"{card_numba[:-12]} {card_numba[-12:-10]}** **** {card_numba[-4:]}"


def get_mask_account(account: str) -> str:
    """Функция принимает на вход номер счета и возвращает его маску"""
    logger.debug(f'Запуск обработки номера счета {account}')
    if type(account) != str:
        logger.error('Номер счета не является строкой')
        raise ValueError("Номер счета должен представлять собой строку")
    if len(account) < 4:
        logger.error('Номер счета содержит менее 4 символов')
        raise ValueError("Номер счета должен содержать минимум 4 символа")
    return f"**{account[-4:]}"


if __name__ == "__main__":
    print(get_mask_card_number("7000792289606361"))
    print(get_mask_account("73654108430135874305"))
