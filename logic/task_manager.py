from .task_model import Task
from time import sleep
from threading import Thread, Lock
from typing import List


class TaskManager(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.tasks = list()
        self.tasks.append(Task("Init", "print('Heartbeat ...')"))
        self.lock = Lock()

    def add_task(self, name: str, task_string: str) -> None:
        with self.lock:
            self.tasks.append(Task(name, task_string))

    def running_loop(self) -> None:
        while True:
            for t in self.tasks:
                print(t)

            # To prevent infinite loop going wild
            sleep(1)

            print("Available tasks: " + str(len(self.tasks)))
            with self.lock:
                for task in self.tasks:
                    if not task.disable:
                        task_string = task.script
                        # Safely sandbox the script
                        exec(task_string, {}, {})

    def run(self) -> None:
        self.running_loop()

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def disable_task(self, id_value: str) -> None:
        for task in self.tasks:
            if task.id == id_value:
                with self.lock:
                    task.disable = True
