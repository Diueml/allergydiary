# === Stage 2: Проверка полей ===
# Project: AllergyDiary
import datetime
from typing import Optional


class EpisodeValidationError(ValueError):
    """Ошибка валидации эпизода аллергии."""


def normalize_trigger(trigger: str) -> str:
    """Нормализует строку триггера: убирает пробелы по краям и в середине."""
    if not isinstance(trigger, str):
        raise EpisodeValidationError("Триггер должен быть строкой.")
    normalized = trigger.strip().lower()
    if not normalized:
        raise EpisodeValidationError("Триггер не может быть пустым.")
    return normalized


def normalize_date(value: str) -> datetime.date:
    """Принимает дату в формате ДД.ММ.ГГГГ и возвращает объект datetime.date."""
    if not isinstance(value, str):
        raise EpisodeValidationError("Дата должна быть строкой.")
    cleaned = value.strip()
    try:
        day, month, year = cleaned.split(".")
        return datetime.date(int(year), int(month), int(day))
    except (ValueError, TypeError):
        raise EpisodeValidationError(
            "Дата должна быть в формате ДД.ММ.ГГГГ, например: 15.06.2024."
        )


def normalize_severity(value: str) -> str:
    """Приводит уровень тяжести к допустимому набору значений."""
    allowed = {
        "1": "легкая",
        "2": "средняя",
        "3": "сильная",
        "4": "очень сильная",
    }
    if not isinstance(value, str):
        raise EpisodeValidationError("Тяжесть должна быть строкой.")
    key = value.strip().lower()
    if key not in allowed:
        raise EpisodeValidationError(
            "Тяжесть должна быть 1-4: легкая, средняя, сильная, очень сильная."
        )
    return allowed[key]


def normalize_duration(value: int) -> int:
    """Нормализует длительность эпизода в минутах (от 1 до 480)."""
    if not isinstance(value, int) or isinstance(value, bool):
        raise EpisodeValidationError("Длительность должна быть целым числом.")
    if value < 1:
        raise EpisodeValidationError(
            "Длительность должна быть не меньше 1 минуты."
        )
    if value > 480:
        raise EpisodeValidationError(
            "Длительность не может превышать 480 минут (8 часов)."
        )
    return value


def validate_episode(
    date: str,
    trigger: str,
    severity: str,
    duration: int,
) -> dict:
    """Валидирует и нормализует поля эпизода, возвращая готовый словарь."""
    normalized_date = normalize_date(date)
    normalized_trigger = normalize_trigger(trigger)
    normalized_severity = normalize_severity(severity)
    normalized_duration = normalize_duration(duration)
    return {
        "date": normalized_date,
        "trigger": normalized_trigger,
        "severity": normalized_severity,
        "duration": normalized_duration,
    }


if __name__ == "__main__":
    print(validate_episode("15.06.2024", "  Пыльца берёзы  ", "3", "90"))
    print(validate_episode("2024-06-20", "Пыльца", "средняя", "2"))
    try:
        validate_episode("31.02.2024", "Пыльца", "5", "100")
    except EpisodeValidationError as error:
        print(error)
