import pytest
from base.assets.get_assets import Resources


@pytest.fixture(scope="session", autouse=True)
def res(request):
    """
    create uiautomator device instance for all test cases
    """
    return Resources()
