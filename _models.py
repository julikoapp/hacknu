from typing import List

class Operator:
    def __init__(self, id: int, email: str, 
                 first_name: str, second_name: str, father_name: str,
                 number: str, password: str) -> None:
        self.id  = id
        self.email = email
        self.first_name = first_name
        self.second_name = second_name
        self.first_name = father_name
        self.number = number
        self.password = password

class Client:
    def __init__(self, id: int, email: str, 
                 first_name: str, second_name: str, father_name: str,
                 number: str, password: str) -> None:
        self.id  = id
        self.email = email
        self.first_name = first_name
        self.second_name = second_name
        self.first_name = father_name
        self.number = number
        self.password = password
        
class Property:
    def __init__(self, id: int, name: str, address: str,
                 lat: float, lon: float) -> None:
        self.id = id
        self.name = name
        self.address = address
        self.lat = lat
        self.lon = lon

class Brigade:
    def __init__(self, id: int, name: str) -> None:
        self.id = id
        self.name = name
        self.
        
    

class Task:
    def __init__(self, id: int, task_type: str) -> None:
        self.id = id
        self.task_type = task_type