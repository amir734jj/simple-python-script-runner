import uuid


class Task:
    def __init__(self, name: str, script: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.script = script
        self.summery = script[:25]
