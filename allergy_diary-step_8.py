# === Stage 8: Теги ===
# Project: AllergyDiary
from datetime import date


class EpisodeTag:
    def __init__(self, name: str, color: str = "#888888"):
        self.name = name
        self.color = color

    def __repr__(self):
        return f"EpisodeTag(name={self.name!r}, color={self.color!r})"


class EpisodeTags:
    def __init__(self):
        self._tags = {}

    def add(self, name: str, color: str = "#888888") -> EpisodeTag:
        if not name:
            raise ValueError("tag name cannot be empty")
        if not self._tags:
            self._tags[name] = EpisodeTag(name, color)
        else:
            for tag in self._tags.values():
                if tag.name.lower() == name.lower():
                    tag.color = color
                    return tag
            self._tags[name] = EpisodeTag(name, color)
        return self._tags[name]

    def remove(self, name: str) -> bool:
        if name in self._tags:
            del self._tags[name]
            return True
        return False

    def has(self, name: str) -> bool:
        for tag in self._tags.values():
            if tag.name.lower() == name.lower():
                return True
        return False

    def find(self, name: str) -> EpisodeTag | None:
        for tag in self._tags.values():
            if tag.name.lower() == name.lower():
                return tag
        return None

    def all(self) -> list[EpisodeTag]:
        return list(self._tags.values())

    def names(self) -> list[str]:
        return [tag.name for tag in self._tags.values()]


class EpisodeTagManager:
    def __init__(self):
        self._tags: EpisodeTags | None = None

    def tags(self) -> EpisodeTags:
        if self._tags is None:
            self._tags = EpisodeTags()
        return self._tags
