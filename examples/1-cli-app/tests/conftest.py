import random

import pytest

from tasks.models import Task

RANDOM_TASKS = (
    'Do something',
    'Do nothing',
    'Sleep',
    'Eat',
    'Work',
    'Random',
    'Rage quit',
)


def generate_random_task():
    return Task(random.randint(1, 100), random.choice(RANDOM_TASKS))


@pytest.fixture
def random_task():
    """Fixture to create a random task."""
    return generate_random_task()


@pytest.fixture
def random_tasks():
    """Fixture factory which create random tasks."""
    def generate():
        return generate_random_task()
    return generate
