from datetime import date, timedelta
import pytest
from tasks import Task, TaskList
from calendars import CalendarStub

def test_task_becomes_overdue():
    # Set a fixed "today" date
    fixed_today = date(2025, 5, 17)
    calendar_stub = CalendarStub(fixed_today)

    # Create a task due tomorrow (relative to fixed_today)
    tomorrow = fixed_today + timedelta(days=1)
    task = Task('some description', tomorrow)

    # Pass the stub calendar to TaskList
    tasks = TaskList(calendar_stub)
    tasks.add_task(task)

    # Initially, task is not overdue
    assert tasks.overdue_tasks == []

    # Move time forward by 2 days
    calendar_stub.today = fixed_today + timedelta(days=2)

    # Now task should be overdue
    assert tasks.overdue_tasks == [task]