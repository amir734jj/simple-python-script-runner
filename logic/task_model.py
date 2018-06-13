import uuid
from datetime import datetime


class Task:
    def __init__(self, name: str, script: str, cron_time: str):
        self.id: str = str(uuid.uuid4())
        self.name: str = name
        self.script: str = script
        self.summery: str = script[:25]
        self.disable: bool = False
        self.next: datetime = None
        self.cron_time: str = cron_time
        self.last_ran: datetime = None

    def execute(self, callback=None):
        if not self.disable:
            self.last_ran = datetime.now()
            print("STARTED {0}".format(self.name))

            # Safely sandbox the script
            exec(self.script, {}, {})

            print("FINISHED {0}".format(self.name))

            # Call the callback
            if callback is not None:
                callback()

    def __str__(self):
        return self.name + "\t" + str(self.disable)
