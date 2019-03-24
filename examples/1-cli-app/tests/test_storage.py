import datetime
from io import StringIO

from tasks import storage
from tasks.models import Task


def test_serialize_task():
    task = Task(1, "Test", datetime.datetime(2018, 1, 1, 10, 0))
    task_creation_date = task.creation_date
    task_time = task_creation_date.strftime("%x %X")

    serialized_task = storage.serialize_task(task)
    assert serialized_task["task_id"] == task.task_id
    assert serialized_task["title"] == task.title
    assert serialized_task["done"] == task.done
    assert serialized_task["creation_date"] == task_time


def test_deserialize_task():
    task = Task(1, "Test")
    ser_task = storage.serialize_task(task)
    deser_task = storage.deserialize_task(ser_task)
    assert deser_task.task_id == task.task_id
    assert deser_task.done == task.done
    assert deser_task.title == task.title


def test_serialize_tasks(random_tasks):
    tasks = [random_tasks() for _ in range(100)]
    ser_tasks = storage.serialize_tasks(tasks)
    assert len(tasks) == len(ser_tasks)


def test_deserialize_tasks(random_tasks):
    tasks = [random_tasks() for _ in range(100)]
    ser_tasks = storage.serialize_tasks(tasks)
    new_tasks = storage.deserialize_tasks(ser_tasks)
    assert len(ser_tasks) == len(tasks) == len(new_tasks)
    assert [t.task_id for t in tasks] == [t.task_id for t in new_tasks]
    assert [t.title for t in tasks] == [t.title for t in new_tasks]


def test_write_to_stream(random_tasks):
    tasks = [random_tasks() for _ in range(100)]
    stream = StringIO()
    storage.write_tasks_to_stream(tasks, stream)

    file_content = stream.getvalue()
    assert len(file_content) > 0


def test_read_from_stream(random_tasks):
    tasks = [random_tasks() for _ in range(100)]
    stream = StringIO()
    storage.write_tasks_to_stream(tasks, stream)

    # Seek start
    stream.seek(0)

    new_tasks = storage.read_tasks_from_stream(stream)
    assert len(new_tasks) == len(tasks)
