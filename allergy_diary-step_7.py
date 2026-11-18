# === Stage 7: Генерация идентификаторов ===
# Project: AllergyDiary
PREFIX = "ad"


def generate_unique_id(prefix: str, existing: list[str]) -> str:
    candidate = f"{prefix}-{len(existing) + 1}"
    attempt = candidate
    guard = 0
    while candidate in existing:
        guard += 1
        candidate = f"{prefix}-{len(existing) + 1}-{guard}"
        if guard > 1000:
            raise ValueError("Не удалось сгенерировать уникальный идентификатор")
    return candidate


def make_unique_id(prefix: str, existing: list[str]) -> str:
    return generate_unique_id(prefix, existing)
