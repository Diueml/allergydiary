# === Stage 6: Связи между сущностями ===
# Project: AllergyDiary
def get_episode_symptoms(episode, symptoms_by_id=None):
    """
    Возвращает список симптомов для заданного эпизода.
    episode: объект с полем 'symptoms' (список идентификаторов) или None.
    symptoms_by_id: словарь id -> объект симптома (опционально).
    """
    if symptoms_by_id is None:
        symptoms_by_id = {}
    episode_symptoms = []
    if episode is None:
        return episode_symptoms
    for sym_id in episode.get('symptoms', []):
        if sym_id in symptoms_by_id:
            episode_symptoms.append(symptoms_by_id[sym_id])
        else:
            raise KeyError("Симптом с id %s не найден" % sym_id)
    return episode_symptoms


def check_episode_symptom_integrity(episode, symptoms_by_id=None):
    """
    Проверяет целостность связи эпизод -> симптомы.
    Возвращает True, если все ссылки валидны, иначе False.
    """
    if symptoms_by_id is None:
        symptoms_by_id = {}
    if episode is None:
        return True
    for sym_id in episode.get('symptoms', []):
        if sym_id not in symptoms_by_id:
            return False
    return True


def build_symptom_index(symptoms):
    """
    Строит словарь id -> симптом из списка симптомов.
    """
    index = {}
    for symptom in symptoms:
        index[symptom['id']] = symptom
    return index


if __name__ == '__main__':
    episode_data = {
        'id': 1,
        'date': '2024-05-15',
        'trigger': 'пыльца',
        'severity': 3,
        'duration': 720,
        'symptoms': [101, 102, 999],
    }
    symptom_list = [
        {'id': 101, 'name': 'зуд глаз'},
        {'id': 102, 'name': 'чихание'},
    ]
    symptom_index = build_symptom_index(symptom_list)
    symptoms = get_episode_symptoms(episode_data, symptom_index)
    print("Симптомы эпизода:", symptoms)
    integrity_ok = check_episode_symptom_integrity(episode_data, symptom_index)
    print("Целостность связи:", integrity_ok)
