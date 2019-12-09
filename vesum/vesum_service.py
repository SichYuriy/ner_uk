from pymongo import MongoClient
from flask import current_app
import os
import logging
logger = logging.getLogger(__name__)

MONGO_URL = ('VESUM_MONGO_DB_URL' in os.environ and os.environ['VESUM_MONGO_DB_URL']) or 'localhost:27017'
DB_NAME = ('VESUM_DB_NAME' in os.environ and os.environ['VESUM_DB_NAME']) or'natasha-uk-database'
BUFFER_LIMIT = 10000
client = MongoClient(MONGO_URL, maxPoolSize=20)


class VesumService:
    def find_by_word_form(self, word_form):
        return client[DB_NAME]['vesum-entry'].find({'word': word_form})


vesum_service = VesumService()
