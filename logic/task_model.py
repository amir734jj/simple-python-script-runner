import uuid


class Task:
    def __init__(self, name: str, script: str):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.script: str = script
        self.summery: str = script[:25]
