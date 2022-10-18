import os

import pytest
from dotenv import load_dotenv

from src.lotr.endpoints import LordOfTheRings

load_dotenv()


@pytest.yield_fixture(scope='session', autouse=True)
def get_client():
    access_token = os.environ.get('ACCESS_TOKEN')
    client = LordOfTheRings(access_token=access_token)
    yield client
