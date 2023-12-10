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


@app.route('/candidate/<int:candidate_id>')
def page_candidate(candidate_id: int) -> str:
    """
    Возвращает страницу кандидата.

    Вывод информации о кандидате по его id.

    Возвращаемое значение:
            str: Информация о кандидатe.
    """
    result_candidate = candidates.get_candidate(candidate_id)
    if not result_candidate:
        return 'Кандидата с таким id нет'
    return render_template('card.html', result_candidate=result_candidate)


if __name__ == '__main__':
    app.run()
