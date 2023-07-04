import pytest

from engine.engine2d import Engine2D


@pytest.fixture()
def engine():
    engine = Engine2D()
    yield engine

