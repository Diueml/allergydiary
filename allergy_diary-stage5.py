# === Stage 5: Связанная сущность ===
# Project: AllergyDiary
SYMPTOM_FIELDS = ("name", "severity", "body_area")
BODY_AREAS = (
    "eyes",
    "nose",
    "throat",
    "skin",
    "lungs",
    "tongue",
    "other",
)
SEVERITIES = ("mild", "moderate", "severe")


class Symptom:
    def __init__(self, name, severity="mild", body_area="other"):
        if not name:
            raise ValueError("name is required")
        if severity not in SEVERITIES:
            raise ValueError(f"severity must be one of {SEVERITIES}")
        if body_area not in BODY_AREAS:
            raise ValueError(f"body_area must be one of {BODY_AREAS}")
        self.id = self._generate_id()
        self.name = name
        self.severity = severity
        self.body_area = body_area

    @staticmethod
    def _generate_id():
        import random
        return f"SYM{random.randint(1000, 9999)}"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "severity": self.severity,
            "body_area": self.body_area,
        }

    def __repr__(self):
        return f"Symptom(id={self.id!r}, name={self.name!r}, severity={self.severity!r}, body_area={self.body_area!r})"


class SymptomStore:
    def __init__(self):
        self._symptoms = {}

    def add_symptom(self, name, severity="mild", body_area="other"):
        symptom = Symptom(name, severity, body_area)
        self._symptoms[symptom.id] = symptom
        return symptom

    def get_symptom(self, symptom_id):
        return self._symptoms.get(symptom_id)

    def all_symptoms(self):
        return list(self._symptoms.values())
