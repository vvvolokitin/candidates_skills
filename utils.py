import json


class Candidates:
    """
    Класс кандидатов.

    Атрибуты:
        candidates (list[dict]): Список всех кандидатов.
    Методы:
        load_candidates_from_json: Возвращает информацию о всех кандидатах.
    """

    def __init__(self, candidates: str) -> None:
        """
        Устанавливает атрибуты для объекта класса Candidates.

        Параметры:
            candidates: (str): Адрес json файлы содержащего информацию о
            кандидатах.

        Возвращаемое значение:
            None.
        """
        with open(candidates, 'r', encoding='utf-8') as file:
            self.candidates = json.load(file)

    def load_candidates_from_json(self) -> list[dict]:
        """
        Возвращает список кандидатов с их характерситиками.

        Возвращаемое значение:
                list[dict]: Информация о кандидатах.
        """
        return self.candidates

    def get_candidate(self, candidate_id: int):
        """
        Возвращает одного кандидата по его id.

        Параметры:
            candidate_id: (int): id кандидата.

        Возвращаемое значение:
                candidate (dict): Информация о кандидате.
        """
        for candidate in self.load_candidates_from_json():
            if candidate['id'] == candidate_id:
                return candidate
        return None

    def get_candidates_by_name(self, name: str) -> list[dict]:
        """
        Возвращает кандидатов по имени.

        Параметры:
            name (str): Имя кандидата.

        Возвращаемое значение:
                candidates_by_name (list[dict]): Информация о кандидатах.
        """
        candidates_by_name: list[dict] = []
        for candidates in self.load_candidates_from_json():
            if name.lower() in candidates['name'].lower():
                candidates_by_name.append(candidates)
        return candidates_by_name

    def get_candidates_by_skill(self, skill: str) -> list[dict]:
        """
        Возвращает кандидатов по навыку.

        Параметры:
            skill (str): Навык кандидата.

        Возвращаемое значение:
                candidates_by_skill (list[dict]): Информация о кандидатах.
        """
        candidates_by_skill: list[dict] = []
        for candidates in self.load_candidates_from_json():
            if skill.lower() in candidates['skills'].lower():
                candidates_by_skill.append(candidates)
        return candidates_by_skill
