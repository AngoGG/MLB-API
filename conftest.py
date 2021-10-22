from _pytest.config.argparsing import Parser
from _pytest.python import Function
import pytest


def pytest_addoption(parser: Parser) -> None:
    parser.addoption(
        '--integ',
        action='store_true',
        help='Run integration tests with all the others (inactive by default)',
    )


def pytest_runtest_setup(item: Function) -> None:
    if 'integ' in item.keywords and not item.config.getoption('--integ'):
        pytest.skip('need --integ option to run this test')
