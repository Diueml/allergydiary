# === Stage 12: Слияние записей ===
# Project: AllergyDiary
from __future__ import annotations


class Episode:
    """Запись эпизода аллергии.

    Поля: дата (str), триггер (str), тяжесть (int), длительность (int),
    симптомы (list[str]).
    """

    def __init__(self, date: str, trigger: str, severity: int,
                 duration: int, symptoms: list[str] | None = None) -> None:
        self.date = date
        self.trigger = trigger
        self.severity = severity
        self.duration = duration
        self.symptoms: list[str] = list(symptoms) if symptoms else []

    def __repr__(self) -> str:
        return (
            f"Episode(date={self.date!r}, trigger={self.trigger!r}, "
            f"severity={self.severity}, duration={self.duration}, "
            f"symptoms={self.symptoms!r})"
        )


def _pick_winner(field: str, a: object, b: object,
                 reverse: bool = False) -> object:
    """Выбрать победителя для одного поля сравнения a/b.

    reverse=True — победит максимальное значение, иначе — минимальное.
    """
    if a == b:
        return a
    if reverse:
        return a if a > b else b
    return a if a < b else b


def combine_episodes(first: Episode, second: Episode, *,
                     date_mode: str = "earlier",
                     severity_mode: str = "higher",
                     duration_mode: str = "longer",
                     trigger_mode: str = "first",
                     symptoms_mode: str = "union") -> Episode:
    """Объединить две записи эпизода с выбором победителя для каждого поля.

    date_mode:  "earlier" | "later"
    severity_mode:  "lower" | "higher"
    duration_mode:  "shorter" | "longer"
    trigger_mode:  "first" | "second"
    symptoms_mode: "union" | "intersection"
    """
    if date_mode == "earlier":
        date = _pick_winner("date", first.date, second.date, reverse=False)
    elif date_mode == "later":
        date = _pick_winner("date", first.date, second.date, reverse=True)
    else:
        raise ValueError("date_mode должен быть 'earlier' или 'later'")

    if severity_mode == "lower":
        severity = _pick_winner("severity", first.severity, second.severity,
                                reverse=False)
    elif severity_mode == "higher":
        severity = _pick_winner("severity", first.severity, second.severity,
                                reverse=True)
    else:
        raise ValueError("severity_mode должен быть 'lower' или 'higher'")

    if duration_mode == "shorter":
        duration = _pick_winner("duration", first.duration, second.duration,
                                reverse=False)
    elif duration_mode == "longer":
        duration = _pick_winner("duration", first.duration, second.duration,
                                reverse=True)
    else:
        raise ValueError("duration_mode должен быть 'shorter' или 'longer'")

    if trigger_mode == "first":
        trigger = first.trigger
    elif trigger_mode == "second":
        trigger = second.trigger
    else:
        raise ValueError("trigger_mode должен быть 'first' или 'second'")

    if symptoms_mode == "union":
        symptoms = sorted(set(first.symptoms) | set(second.symptoms))
    elif symptoms_mode == "intersection":
        symptoms = sorted(set(first.symptoms) & set(second.symptoms))
    else:
        raise ValueError("symptoms_mode должен быть 'union' или 'intersection'")

    return Episode(date=date, trigger=trigger, severity=severity,
                   duration=duration, symptoms=symptoms)


if __name__ == "__main__":
    a = Episode("2024-05-01", "пыльца", 3, 120, ["зуд", "чихание"])
    b = Episode("2024-05-03", "пыльца", 5, 200, ["зуд", "отёк"])
    merged = combine_episodes(
        a, b,
        date_mode="earlier",
        severity_mode="higher",
        duration_mode="longer",
        trigger_mode="first",
        symptoms_mode="union",
    )
    print(merged)
