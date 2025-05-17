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
    def __init__(self, calendar=None):
        from calendars import Calendar
        self.__calendar = calendar if calendar else Calendar()
        self.__tasks = []

    def add_task(self, task):
        if task.due_date < self.__calendar.today:
            raise RuntimeError("Cannot add task with due date in the past")
        self.__tasks.append(task)

    def __len__(self):
        return len(self.__tasks)

    @property
    def finished_tasks(self):
        return [task for task in self.__tasks if task.finished]

    @property
    def due_tasks(self):
        return [task for task in self.__tasks if not task.finished]

    @property
    def overdue_tasks(self):
        today = self.__calendar.today
        return [task for task in self.__tasks if not task.finished and task.due_date < today]