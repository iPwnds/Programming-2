from datetime import date, timedelta
import pytest
from tasks import Task, TaskList
from calendars import CalendarStub

def setup_function():
    global today, tomorrow, yesterday, calendar, sut

    today = date(2000, 1, 1)
    tomorrow = today + timedelta(days=1)
    yesterday = today - timedelta(days=1)
    calendar = CalendarStub(today)
    sut = TaskList(calendar)


def test_creation():
    # Arrange is done in setup_function

    # Act & Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future():
    # Arrange
    task = Task('future task', tomorrow)

    # Act
    sut.add_task(task)

    # Assert
    assert len(sut) == 1
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks
    assert sut.overdue_tasks == []

def test_adding_task_with_due_day_in_past():
    # Arrange
    task = Task('past task', yesterday)

    # Act & Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)

def test_task_becomes_finished():
    # Arrange
    task = Task('task to finish', tomorrow)
    sut.add_task(task)

    # Pre-assertion: task is due and not finished
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks

    # Act
    task.finished = True

    # Assert
    assert task not in sut.due_tasks
    assert task in sut.finished_tasks