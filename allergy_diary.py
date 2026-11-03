# === Stage 1: Каркас модуля ===
# Project: AllergyDiary
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from typing import List


class Trigger(str, Enum):
    POLLEN = "pollen"
    DUST_MITE = "dust_mite"
    PET_DANDRUFF = "pet_dandruff"
    FOOD = "food"
    MEDICATION = "medication"
    OTHER = "other"


class Severity(str, Enum):
    NONE = 0
    MILD = 1
    MODERATE = 2
    SEVERE = 3

    def label(self) -> str:
        return {
            Severity.NONE: "none",
            Severity.MILD: "mild",
            Severity.MODERATE: "moderate",
            Severity.SEVERE: "severe",
        }[self]


@dataclass
class Episode:
    date: date
    trigger: Trigger
    severity: Severity
    duration_minutes: int
    symptoms: List[str] = field(default_factory=list)

    def summary(self) -> str:
        return (
            f"{self.date} | {self.trigger.value} | "
            f"{self.severity.label()} | {self.duration_minutes} мин | "
            f"{len(self.symptoms)} симптомов"
        )


def sample_episodes() -> List[Episode]:
    return [
        Episode(
            date=date(2024, 4, 12),
            trigger=Trigger.POLLEN,
            severity=Severity.MODERATE,
            duration_minutes=120,
            symptoms=["sneezing", "itchy_eyes"],
        ),
        Episode(
            date=date(2024, 4, 19),
            trigger=Trigger.DUST_MITE,
            severity=Severity.MILD,
            duration_minutes=45,
            symptoms=["runny_nose"],
        ),
        Episode(
            date=date(2024, 5, 3),
            trigger=Trigger.FOOD,
            severity=Severity.SEVERE,
            duration_minutes=60,
            symptoms=["swelling", "hives"],
        ),
    ]


def main() -> None:
    episodes = sample_episodes()
    print("AllergyDiary — демо эпизоды:")
    for episode in episodes:
        print("  " + episode.summary())


if __name__ == "__main__":
    main()
