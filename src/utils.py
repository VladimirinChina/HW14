import json
from typing import Any, List, cast


def load_json_file(path: str) -> List[Any]:
    """
    Загружает данные из JSON-файла.

    Функция выполняет только чтение и парсинг JSON без какой-либо
    бизнес-логики или преобразования данных.

    :param path: Путь к JSON-файлу
    :return: Список данных из JSON
    :raises FileNotFoundError: если файл не найден
    :raises json.JSONDecodeError: если файл содержит некорректный JSON
    """
    with open(path, "r", encoding="utf-8") as file:
        return cast(List[Any], json.load(file))
