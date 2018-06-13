from threading import Timer
from croniter import croniter
from datetime import datetime
from .task_model import Task


class TaskScheduler:
    def __init__(self, task: Task):
        self.task = task
        self.stop = False
        now = datetime.now()
        self.time_iter = croniter(task.cron_time, now)
        # self.time_iter.get_next(datetime)

    def reschedule(self):
        if not self.stop:
            self.schedule()

    def schedule(self) -> None:
        self.task.next = self.time_iter.get_next(datetime)
        delay = (self.task.next - datetime.now()).total_seconds()
        print("SCHEDULED AT: {0}".format(self.task.next))

        Timer(delay, lambda: self.task.execute(callback=lambda: self.reschedule())).start()

    def unschedule(self):
        self.stop = True
        self.task.disable = True
