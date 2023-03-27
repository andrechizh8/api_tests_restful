import pytest
import os
from dotenv import load_dotenv
from utils.base_session import BaseSession

load_dotenv()
web_url = os.getenv("WEB_URL")
login = os.getenv("LOGIN")
password = os.getenv("PASSWORD")


@pytest.fixture(scope="session")
def restful():
    return BaseSession(web_url)


@pytest.fixture(scope="session")
def get_token(restful):
    """Fixture return  token for using in tests"""
    response = restful.post("/auth", json={"username": login, "password": password})
    token = response.json()["token"]

    return token
