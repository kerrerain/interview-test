import pytest
from onepoint.log import init_log, log


@pytest.fixture(scope="session", autouse=True)
def context():
    init_log()
    log.debug("Test logger initialized")
