from datetime import date, timedelta
import pytest
from tasks import Task, TaskList
from calendars import CalendarStub

@pytest.fixture
def today():
    return date(2000, 1, 1)

@pytest.fixture
def tomorrow(today):
    return today + timedelta(days=1)

@pytest.fixture
def yesterday(today):
    return today - timedelta(days=1)

@pytest.fixture
def calendar(today):
    return CalendarStub(today)

@pytest.fixture
def sut(calendar):
    return TaskList(calendar)


def test_creation(sut):
    assert len(sut) == 0
    assert sut.due_tasks == []
    assert sut.overdue_tasks == []
    assert sut.finished_tasks == []

def test_adding_task_with_due_day_in_future(sut, tomorrow):
    task = Task('future task', tomorrow)
    sut.add_task(task)

    assert len(sut) == 1
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks
    assert sut.overdue_tasks == []

def test_adding_task_with_due_day_in_past(sut, yesterday):
    task = Task('past task', yesterday)

    with pytest.raises(RuntimeError):
        sut.add_task(task)

def test_task_becomes_finished(sut, tomorrow):
    task = Task('task to finish', tomorrow)
    sut.add_task(task)

    # Pre-assertion
    assert task in sut.due_tasks
    assert task not in sut.finished_tasks

    # Act
    task.finished = True

    # Assert
    assert task not in sut.due_tasks
    assert task in sut.finished_tasks