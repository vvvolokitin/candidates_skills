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

    def load_candidates_from_json(self):
        """
        Возвращает список кандидатов с их характерситиками.

        Возвращаемое значение:
                list[dict]: Информация о кандидатах.
        """
        return self.candidates

    def get_candidate(self, candidate_id):
        """
        Возвращает одного кандидата по его id.

        Возвращаемое значение:
                candidate (dict): Информация о кандидате.
        """
        for candidate in self.load_candidates_from_json():
            if candidate['id'] == candidate_id:
                return candidate
