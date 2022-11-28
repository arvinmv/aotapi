import logging
from aotapi.rest_adapter import RestAdapter
from aotapi.exceptions import AotApiException
from aotapi.models import *


class AotApi:
    def __init__(self, hostname: str = 'api-attack-on-titan.herokuapp.com', ver: str = 'v1',
                 ssl_verify: bool = True, logger: logging.Logger = None):
        self._rest_adapter = RestAdapter(hostname, ver, ssl_verify, logger)

    def get_character(self, index) -> Characters:
        result = self._rest_adapter.get(endpoint='/characters')
        character = Characters(**result.data[index])
        return character

    def get_all_characters(self) -> List:
        result = self._rest_adapter.get(endpoint='/characters')
        all_characters = result.data
        return all_characters

    def get_titan(self, index) -> Titans:
        result = self._rest_adapter.get(endpoint='/titans')
        titan = Titans(**result.data[index])
        return titan

    def get_all_titans(self) -> List:
        result = self._rest_adapter.get(endpoint='/titans')
        all_titans = result.data
        return all_titans
