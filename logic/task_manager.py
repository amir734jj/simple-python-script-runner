import asyncio
from threading import Thread
from .task_model import Task
from typing import List


class TaskManager:

    def __init__(self):
        self.tasks = list()
        self.tasks.append(Task("Init", "print('Heartbeat ...')"))
        Thread(target=lambda x: self.start_loop(), args=([""])).start()

    def add_task(self, name: str, task_string: str) -> None:
        self.tasks.append(Task(name, task_string))

    @asyncio.coroutine
    def running_loop(self) -> None:
        while True:
            for task in list(self.tasks):
                task_string = task.script
                # Safely sandbox the script
                exec(task_string, {}, {})
                yield from asyncio.sleep(1)

    def start_loop(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(self.running_loop())

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def delete_task(self, id_value: str) -> None:
        self.tasks = [task for task in self.tasks if task.id != id_value]
