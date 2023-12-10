import flask

from utils import Candidates


if __name__ == '__main__':
    candidates = Candidates('candidates.json')
    print(candidates.load_candidates_from_json())
