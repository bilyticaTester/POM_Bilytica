import pytest


#this fixture is defined in testConfig
@pytest.mark.usefixtures("init_driver")
class BaseTest:
    pass