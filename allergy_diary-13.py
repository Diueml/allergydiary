# === Stage 13: Массовое обновление ===
# Project: AllergyDiary
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, List, Optional


@dataclass
class Episode:
    date: date
    trigger: str
    severity: int
    duration: int
    symptoms: List[str] = field(default_factory=list)


@dataclass
class Preview:
    matched: int
    changes: List[str] = field(default_factory=list)


def _format_change(index: int, old: str, new: str) -> str:
    return f"  эпизод {index}: {old} -> {new}"


def preview_update(
    episodes: Iterable[Episode],
    predicate,
    new_severity=None,
    new_trigger=None,
    new_duration=None,
) -> Preview:
    changed: List[str] = []
    for index, episode in enumerate(episodes):
        if not predicate(episode):
            continue
        old_severity = str(episode.severity)
        old_trigger = episode.trigger
        old_duration = str(episode.duration)
        if new_severity is not None:
            episode.severity = new_severity
            old_severity = str(new_severity)
        if new_trigger is not None:
            episode.trigger = new_trigger
            old_trigger = new_trigger
        if new_duration is not None:
            episode.duration = new_duration
            old_duration = str(new_duration)
        changed.append(
            _format_change(index, old_severity, old_trigger, old_duration)
        )
    return Preview(matched=len(changed), changes=changed)


def apply_update(
    episodes: List[Episode],
    predicate,
    new_severity=None,
    new_trigger=None,
    new_duration=None,
) -> int:
    preview = preview_update(
        episodes, predicate, new_severity, new_trigger, new_duration
    )
    for episode in episodes:
        if not predicate(episode):
            continue
        if new_severity is not None:
            episode.severity = new_severity
        if new_trigger is not None:
            episode.trigger = new_trigger
        if new_duration is not None:
            episode.duration = new_duration
    return preview.matched
