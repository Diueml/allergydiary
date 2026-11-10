# === Stage 4: Удаление и восстановление ===
# Project: AllergyDiary
from datetime import date


class Episode:
    def __init__(self, episode_id, date, trigger, severity, duration,
                 symptom_ids=None, is_deleted=False):
        self.id = episode_id
        self.date = date
        self.trigger = trigger
        self.severity = severity
        self.duration = duration
        self.symptom_ids = symptom_ids or []
        self.is_deleted = is_deleted

    def delete(self):
        self.is_deleted = True

    def restore(self):
        self.is_deleted = False

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date.isoformat(),
            "trigger": self.trigger,
            "severity": self.severity,
            "duration": self.duration,
            "symptom_ids": list(self.symptom_ids),
            "is_deleted": self.is_deleted,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            episode_id=data["id"],
            date=date.fromisoformat(data["date"]),
            trigger=data["trigger"],
            severity=data["severity"],
            duration=data["duration"],
            symptom_ids=data.get("symptom_ids", []),
            is_deleted=data.get("is_deleted", False),
        )


class EpisodeStore:
    def __init__(self):
        self._episodes = {}

    def add(self, episode):
        self._episodes[episode.id] = episode

    def get(self, episode_id):
        return self._episodes.get(episode_id)

    def list_active(self):
        return [e for e in self._episodes.values() if not e.is_deleted]

    def list_deleted(self):
        return [e for e in self._episodes.values() if e.is_deleted]

    def delete(self, episode_id):
        episode = self._episodes.get(episode_id)
        if episode:
            episode.delete()

    def restore(self, episode_id):
        episode = self._episodes.get(episode_id)
        if episode:
            episode.restore()

    def trash(self):
        return self.list_deleted()

    def restore_all(self):
        for episode in self.list_deleted():
            episode.restore()
