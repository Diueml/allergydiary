# === Stage 10: Быстрые фильтры ===
# Project: AllergyDiary
from datetime import date, datetime, timedelta


def _parse_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    return datetime.fromisoformat(value).date()


def _today():
    return _parse_date(date.today())


def _start_of_week(day):
    if isinstance(day, datetime):
        day = day.date()
    return day - timedelta(days=day.weekday())


def episodes_today(episodes):
    return [ep for ep in episodes if _parse_date(ep.get("date")) == _today()]


def episodes_this_week(episodes):
    today = _today()
    start = _start_of_week(today)
    end = start + timedelta(days=6)
    return [ep for ep in episodes if start <= _parse_date(ep.get("date")) <= end]


def episodes_expired(episodes, reference=None):
    if reference is None:
        reference = _today()
    if isinstance(reference, datetime):
        reference = reference.date()
    return [ep for ep in episodes if _parse_date(ep.get("date")) < reference]
