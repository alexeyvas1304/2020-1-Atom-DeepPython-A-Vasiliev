from loguru import logger
from random import randint


class IncorrectLengthException(Exception):
    pass


@logger.catch
def get_new_list_tricky(lst):
    logger.add("tricky_realization.log")
    logger.info("Начало функции")
    logger.info("Вычисление длины списка")
    length = len(lst)
    if length < 2:
        logger.error('length < 2')
        raise IncorrectLengthException()
    prefixes = [1] + [None] * (length - 1)
    logger.info("Вычисление префиксов")
    for i in range(length - 1):
        logger.info(f"Вычисление префикса {i}")
        prefixes[i + 1] = prefixes[i] * lst[i]
    suffix = 1
    logger.info("Окончательный расчет")
    for i in range(length - 1, -1, -1):
        logger.info(f"Вычисление значения и пересчет суффикса {i}")
        prefixes[i] *= suffix
        suffix *= lst[i]
    logger.info("Возвращение значения")
    return prefixes


if __name__ == '__main__':
    get_new_list_tricky([randint(1, 10 ** 7) for _ in range(2000)])
