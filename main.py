from flask import Flask, render_template

from utils import Candidates

app = Flask(__name__)
candidates = Candidates('candidates.json')


@app.route('/')
def main_page():
    """
    Возвращает главную страницу.

    Вывод на главную страницу иформацию о всех кандидатах.

    Переменные:
        all_candidates (list[tuple[int, str]]): Список всех кандидатов и их id.

    Возвращаемое значение:
        str: Информация о всех кандидатах.
    """
    all_candidates: list[tuple[int, str]] = []
    for candidate in candidates.load_candidates_from_json():
        all_candidates.append((candidate['id'], candidate['name']))
    return render_template('list.html', all_candidates=all_candidates)


if __name__ == '__main__':
    app.run()
