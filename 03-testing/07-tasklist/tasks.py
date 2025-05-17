from datetime import date


class Task:
    def __init__(self, description: str, due_date: date):
        self._description = description
        self._due_date = due_date
        self.finished = False

    @property
    def description(self):
        return self._description

    @property
    def due_date(self):
        return self._due_date


class TaskList:
    def __init__(self):
        self._tasks = []

    def add_task(self, task: Task):
        if task.due_date < date.today():
            raise RuntimeError("Task due date is in the past")
        self._tasks.append(task)

    def __len__(self):
        return len(self._tasks)

    @property
    def finished_tasks(self):
        return [task for task in self._tasks if task.finished]

    @property
    def due_tasks(self):
        return [task for task in self._tasks if not task.finished]

    @property
    def overdue_tasks(self):
        today = date.today()
        return [task for task in self._tasks if not task.finished and task.due_date < today]