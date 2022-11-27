from typing import List, Dict

class Result:
    def __init__(self, status_code: int, message: str = '', data: List[Dict] = None):
        """
        Result returned from low-level RestAdapter
        :param status_code: Standard HTTP Status code
        :param message: Human readable result
        :param data: Python list of dictionaries (or maybe just a single Dictionary on error)
        """
        self.status_code = int(status_code)
        self.message = str(message)
        self.data = data if data else []

class Characters:
    def __init__(self, id: int, first_name: str, last_name: str, species: str, age: int, height,
                 residence: str, status: str, alias: str):
        self.id = int(id)
        self.first_name = str(first_name)
        self.last_name = str(last_name)
        self.species = str(species)
        self.age = int(age)
        self.height = str(height)
        self.residence = str(residence)
        self.status = str(status)
        self.alias = str(alias)

class Titans:
    def __init__(self, id: int, name: str, other_names: str, abilities: str, current_inheritor: str,
                 former_inheritors: str, allegiance: str):
        self.id = int(id)
        self.name = str(name)
        self.other_names = str(other_names)
        self.abilities = str(abilities)
        self.current_inheritor = str(current_inheritor)
        self.former_inheritors = str(former_inheritors)
        self.allegiance = str(allegiance)