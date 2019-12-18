from flask import Flask
from flask import Response
from flask import request
import os

import json
from api import name_extracting_service
from api import person_extracting_service
from api import date_extracting_service
from api import location_extracting_service

from vesum import vesum_service

app = Flask(__name__)
vesum_service.init_vesum()


@app.route("/")
def hello():
    return "Hello world!"


@app.route('/extract-names-uk', methods=['POST'])
def extract_names_uk():
    articles = json.loads(request.data)
    articles_matches = name_extracting_service.extract_names(articles)
    dto = to_dto(articles_matches, request.args.get('extract_tokens'))
    return Response(json.dumps(dto), mimetype='application/json')


@app.route('/extract-persons-uk', methods=['POST'])
def extract_persons_uk():
    articles = json.loads(request.data)
    articles_matches = person_extracting_service.extract_persons(articles)
    dto = to_dto(articles_matches, request.args.get('extract_tokens'))
    return Response(json.dumps(dto), mimetype='application/json')


@app.route('/extract-dates-uk', methods=['POST'])
def extract_dates_uk():
    articles = json.loads(request.data)
    articles_matches = date_extracting_service.extract_dates(articles)
    dto = to_dto(articles_matches, request.args.get('extract_tokens'))
    return Response(json.dumps(dto), mimetype='application/json')


@app.route('/extract-locations-uk', methods=['POST'])
def extract_locations_uk():
    articles = json.loads(request.data)
    articles_matches = location_extracting_service.extract_locations(articles)
    dto = to_dto(articles_matches, request.args.get('extract_tokens'))
    return Response(json.dumps(dto), mimetype='application/json')


@app.route('/extract-all-uk', methods=['POST'])
def extract_all_uk():
    articles = json.loads(request.data)
    person_matches = person_extracting_service.extract_persons(articles)
    date_matches = date_extracting_service.extract_dates(articles)
    location_matches = location_extracting_service.extract_locations(articles)
    dto = []
    for i in range(len(person_matches)):
        article_matches = []
        article_matches.extend(person_matches[i][0].as_json)
        article_matches.extend(date_matches[i][0].as_json)
        article_matches.extend(location_matches[i][0].as_json)
        if request.args.get('extract_tokens'):
            item = {'matches': article_matches, 'tokens': list(map(lambda token: token.as_json(), person_matches[i][1]))}
        else:
            item = {'matches': article_matches}
        dto.append(item)
    return Response(json.dumps(dto), mimetype='application/json')


@app.route('/refresh-dictionary', methods=['PUT'])
def refresh_dictionary():
    vesum_service.refresh_dictionary(request.args.get('dictionary_url'))
    return 'Refreshed'


def to_dto(articles_matches, extract_tokens):
    if extract_tokens:
        return list(map(
            lambda matches: {'matches': matches[0].as_json,
                             'tokens': list(map(lambda token: token.as_json(), matches[1]))},
            articles_matches))
    else:
        return {'matches': list(map(lambda matches: matches[0].as_json, articles_matches))}


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
