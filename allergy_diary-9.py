# === Stage 9: Группировка ===
# Project: AllergyDiary
from collections import Counter


def group_episodes_by_trigger(
    episodes: list[dict],
    trigger_field: str = "trigger",
) -> dict[str, int]:
    """Группирует эпизоды по полю триггер и считает эпизодов в каждой группе."""
    counts: Counter = Counter()
    for episode in episodes:
        trigger = episode.get(trigger_field)
        if trigger is not None:
            counts[trigger] += 1
    return dict(sorted(counts.items()))


def summarize_trigger_activity(episodes: list[dict]) -> dict[str, int]:
    """Формирует сводку: триггер -> количество эпизодов."""
    return group_episodes_by_trigger(episodes)


def top_triggers(episodes: list[dict], limit: int = 5) -> list[tuple[str, int]]:
    """Возвращает список самых частых триггеров с количеством эпизодов."""
    counts = group_episodes_by_trigger(episodes)
    return counts.most_common(limit)


def analyze_seasonal_triggers(
    episodes: list[dict],
    season_field: str = "season",
    trigger_field: str = "trigger",
) -> dict[str, dict[str, int]]:
    """Группирует эпизоды по сезону и триггеру внутри каждого сезона."""
    grouped: dict[str, dict[str, int]] = {}
    for episode in episodes:
        season = episode.get(season_field)
        trigger = episode.get(trigger_field)
        if season is None or trigger is None:
            continue
        season_groups = grouped.setdefault(season, {})
        season_groups[trigger] = season_groups.get(trigger, 0) + 1
    return grouped


def build_trigger_report(
    episodes: list[dict],
    season_field: str = "season",
    trigger_field: str = "trigger",
) -> str:
    """Собирает текстовый отчёт о распределении триггеров по сезонам."""
    grouped = analyze_seasonal_triggers(episodes, season_field, trigger_field)
    lines: list[str] = []
    for season, triggers in grouped.items():
        lines.append(f"Сезон: {season}")
        for trigger, count in triggers.items():
            lines.append(f"  {trigger}: {count}")
        lines.append("")
    return "\n".join(lines).rstrip()


if __name__ == "__main__":
    sample_episodes: list[dict] = [
        {"date": "2024-04-01", "trigger": "пыльца берёзы", "severity": 3, "duration": 2},
        {"date": "2024-04-10", "trigger": "пыльца берёзы", "severity": 4, "duration": 1},
        {"date": "2024-05-05", "trigger": "пыль", "severity": 2, "duration": 3},
        {"date": "2024-06-12", "trigger": "пыльца берёзы", "severity": 5, "duration": 1},
        {"date": "2024-07-20", "trigger": "пыль", "severity": 3, "duration": 2},
        {"date": "2024-08-15", "trigger": "плесень", "severity": 1, "duration": 1},
    ]

    print(build_trigger_report(sample_episodes))
    print()
    print("Общий по триггерам:", summarize_trigger_activity(sample_episodes))
    print()
    print("Топ триггеров:", top_triggers(sample_episodes))
