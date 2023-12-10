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
