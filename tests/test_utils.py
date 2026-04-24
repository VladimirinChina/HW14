import json
from pathlib import Path

import pytest

from src.utils import load_json_file


def test_load_json_file_success(tmp_path: Path) -> None:
    """Проверка успешной загрузки JSON-файла."""

    data = [{"name": "Категория"}]

    file_path = tmp_path / "test.json"
    file_path.write_text(json.dumps(data), encoding="utf-8")

    result = load_json_file(str(file_path))

    assert result == data


def test_load_json_file_empty(tmp_path: Path) -> None:
    """Проверка работы с пустым JSON."""

    file_path = tmp_path / "empty.json"
    file_path.write_text("[]", encoding="utf-8")

    result = load_json_file(str(file_path))

    assert result == []


def test_load_json_file_not_found() -> None:
    """Проверка ошибки при отсутствии файла."""

    with pytest.raises(FileNotFoundError):
        load_json_file("non_existent_file.json")


def test_load_json_file_invalid_json(tmp_path: Path) -> None:
    """Проверка ошибки при некорректном JSON."""

    file_path = tmp_path / "bad.json"
    file_path.write_text("{ invalid json }", encoding="utf-8")

    with pytest.raises(json.JSONDecodeError):
        load_json_file(str(file_path))
