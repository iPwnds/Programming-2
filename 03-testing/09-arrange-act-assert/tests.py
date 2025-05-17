from datetime import date, timedelta
import pytest
from tasks import Task, TaskList
from calendars import CalendarStub

def test_creation():
    # Arrange
    fixed_today = date(2025, 5, 17)
    calendar = CalendarStub(fixed_today)
    sut = TaskList(calendar)

    # Act & Assert
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future():
    # Arrange
    fixed_today = date(2025, 5, 17)
    future_date = fixed_today + timedelta(days=1)
    calendar = CalendarStub(fixed_today)
    sut = TaskList(calendar)
    task = Task('future task', future_date)

    # Act
    sut.add_task(task)

    # Assert
    assert len(sut) == 1
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks
    assert sut.overdue_tasks == []

def test_adding_task_with_due_day_in_past():
    # Arrange
    fixed_today = date(2025, 5, 17)
    past_date = fixed_today - timedelta(days=1)
    calendar = CalendarStub(fixed_today)
    sut = TaskList(calendar)
    task = Task('past task', past_date)

    # Act & Assert
    with pytest.raises(RuntimeError):
        sut.add_task(task)

def test_task_becomes_finished():
    # Arrange
    fixed_today = date(2025, 5, 17)
    future_date = fixed_today + timedelta(days=1)
    calendar = CalendarStub(fixed_today)
    sut = TaskList(calendar)
    task = Task('task to finish', future_date)
    sut.add_task(task)

    # Pre-assertion: task is due and not finished
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks

    # Act
    task.finished = True

    # Assert
    assert task not in sut.due_tasks
    assert task in sut.finished_tasks