import pytest


@pytest.fixture(scope="session")
def session_fixture():
    return {
        "session_key": 1234
    }


@pytest.fixture(scope="module")
def module_fixture():
    return {
        "module_key": 7890
    }


@pytest.fixture
def function_fixture():
    return {
        "function_key": 1902
    }


def test_fix1(session_fixture, module_fixture, function_fixture):
    # session_fixture va se créer
    # module_fixture va se créer
    # function_fixture va se créer
    pass


def test_fix2():
    # session_fixture existe déja
    # module_fixture existe déja
    # function_fixture va se créer
    pass
