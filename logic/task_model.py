import uuid


class Task:
    def __init__(self, name: str, script: str):
        self.id = str(uuid.uuid4())
        self.name = name
        self.script = script
        self.summery = script[:25]
        self.disable = False

    def __str__(self):
        return self.name  + "\t" + str(self.disable)
