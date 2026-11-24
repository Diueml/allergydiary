# === Stage 11: Поиск дубликатов ===
# Project: AllergyDiary
from datetime import date


def normalize_trigger(trigger):
    if trigger is None:
        return ""
    return trigger.strip().lower()


def normalize_severity(severity):
    if severity is None:
        return ""
    return str(severity).strip().lower()


def normalize_duration(duration):
    if duration is None:
        return ""
    return str(duration).strip()


def normalize_date(day):
    if not isinstance(day, date):
        return ""
    return day.isoformat()


def normalize_episode(episode):
    return (
        normalize_date(episode.get("date")),
        normalize_trigger(episode.get("trigger")),
        normalize_severity(episode.get("severity")),
        normalize_duration(episode.get("duration")),
    )


def find_duplicate_episodes(episodes):
    seen = {}
    duplicates = []
    for episode in episodes:
        key = normalize_episode(episode)
        if key in seen:
            duplicates.append(episode)
        else:
            seen[key] = episode
    return duplicates
