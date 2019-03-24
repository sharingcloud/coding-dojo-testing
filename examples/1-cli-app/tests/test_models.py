import os

import pytest

from tasks.models import TaskManager


@pytest.fixture
def manager():
    return TaskManager()


def test_tasks(tmpdir, manager):
    t1 = manager.add_task("Task")
    t2 = manager.add_task("Task 2")
    assert t1.task_id == 1
    assert t1.title == "Task"
    assert t2.task_id == 2

    # Get task
    assert manager.get_task(1) == t1

    # Show task
    manager.show_task(1)

    # Error
    manager.show_task(3)

    # Show all tasks
    manager.show_tasks()

    # Toggle task
    manager.toggle_task(1)

    # Remove task
    manager.remove_task(1)

    # Rename task
    manager.rename_task(2, "Test")
    assert manager.get_task(2).title == "Test"

    # Export tasks
    export_path = os.path.join(tmpdir, "test.json")
    manager.export_tasks(export_path)
    assert len(manager.task_index.keys()) == 1

    # Import tasks
    manager.remove_task(2)
    manager.import_tasks(export_path)
    assert len(manager.task_index.keys()) == 1

    # Show stats
    manager.show_stats()
