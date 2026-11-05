# === Stage 3: Хранилище в памяти ===
# Project: AllergyDiary
memory_store.py

from datetime import date


class Episode:
    def __init__(self, episode_id, day, trigger, severity, duration):
        self.episode_id = episode_id
        self.day = day
        self.trigger = trigger
        self.severity = severity
        self.duration = duration


class InMemoryEpisodeStore:
    def __init__(self):
        self._episodes = {}

    def add_episode(self, episode):
        if episode.episode_id in self._episodes:
            raise ValueError(f"Episode {episode.episode_id} already exists")
        self._episodes[episode.episode_id] = episode
        return episode

    def get_episode(self, episode_id):
        return self._episodes.get(episode_id)

    def list_episodes(self):
        return list(self._episodes.values())


if __name__ == "__main__":
    store = InMemoryEpisodeStore()
    store.add_episode(Episode("e1", date(2025, 1, 10), "pollen", 3, 2))
    store.add_episode(Episode("e2", date(2025, 1, 11), "dust", 4, 1))
    print(store.get_episode("e1").trigger)
    print(store.list_episodes()[0].day)
