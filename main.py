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
        return (
            'Кандидата с таким id нет <p><a href="/"> Вернуться на главную '
            'страницу</a> </p>'
        )
    return render_template('card.html', result_candidate=result_candidate)


@app.route('/skill/<skill>')
def page_skill(skill: str) -> str:
    """
    Возвращает страницу с кандидатами по навыкам.

    Вывод на страницу иформацию о всех кандидатах с указанными навыками.

    Возвращаемое значение:
            str: Информация о кандидатах.
    """
    result_candidates = candidates.get_candidates_by_skill(skill)
    if not result_candidates:
        return (
            'Кандидатов с таким навыком нет <p><a href="/"> '
            'Вернуться на главную страницу</a> </p>'
        )
    return render_template(
        'skill.html', skill=skill, result_candidates=result_candidates
    )


@app.route('/search/<name>')
def page_search(name: str) -> str:
    """
    Возвращает страницу с кандидатами по имени.

    Вывод на страницу иформацию о всех кандидатах с указанным именем.

    Возвращаемое значение:
            str: Информация о кандидатах.
    """
    result_candidates = candidates.get_candidates_by_name(name)
    if not result_candidates:
        return (
            'Кандидатов с таким именем нет <p><a href="/"> '
            'Вернуться на главную страницу</a> </p>'
        )
    return render_template(
        'search.html', name=name.capitalize(),
        result_candidates=result_candidates
    )


if __name__ == '__main__':
    app.run()
