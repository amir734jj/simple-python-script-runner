from .task_model import Task
from threading import Thread, Lock
from typing import List
from .singleton_mixin import SingletonMixin
from .task_scheduler import TaskScheduler


class TaskManager(SingletonMixin, Thread):

    def __init__(self):
        Thread.__init__(self)
        self.tasks = list()
        self.schedules = dict()
        self.lock = Lock()

    def add_task(self, name: str, task_string: str, cron_time: str) -> None:
        with self.lock:
            task = Task(name, task_string, cron_time)
            self.tasks.append(task)
            self.schedules[task] = TaskScheduler(task)
            self.schedules[task].schedule()

    def running_loop(self) -> None:
        pass
        # while True:
        #     # To prevent infinite loop going wild
        #     sleep(1)
        #
        #     with self.lock:
        #         for task in self.tasks:
        #             if not task.disable:
        #                 task_string = task.script
        #                 # Safely sandbox the script
        #                 exec(task_string, {}, {})

    def run(self) -> None:
        self.running_loop()

    def get_tasks(self) -> List[Task]:
        return self.tasks

    def toggle_task(self, id_value: str) -> None:
        for task in self.tasks:
            if task.id == id_value:
                with self.lock:
                    task.disable = not task.disable
                    if not task.disable:
                        self.schedules[task].schedule()

    def delete_task(self, id_value: str) -> None:
        for task in self.tasks:
            if task.id == id_value:
                with self.lock:
                    self.schedules[task].unschedule()
                    self.tasks.remove(task)
                    del self.schedules[task]
