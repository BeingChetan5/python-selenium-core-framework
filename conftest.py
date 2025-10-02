import pytest
import os
import sys

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append(dir_path)

from test_settings import Settings
from client_api.home.home_labels import HomeLabels
from client_api.home.home_page import HomePage
from client_api.home.home_assertions import HomeAssertions
from core_api.api_helper import CoreApi
from csv import DictReader

ids = []


def pytest_addoption(parser):
    pass


@pytest.fixture(autouse=True, scope="class")
def setup(request):
    request.cls.home_labels = HomeLabels()
    request.cls.api = CoreApi()
    request.cls.home_page = HomePage()
    request.cls.home_assertions = HomeAssertions()

    # Install webdriver
    request.cls.webdriver_path = request.cls.api.install_webdriver("chrome")


@pytest.fixture(autouse=True, scope="class")
def close_browser(request):
    def tear_down():
        print("Tear down initiated.. Closing the browser.")
        request.cls.api.close_browser(request.cls.webdriver_path)

    request.addfinalizer(tear_down)


@pytest.fixture(autouse=True, scope="class")
def launch_browser(request):
    request.cls.webdriver_path.get("https://www.thetestingworld.com/testings")


def get_data():
    print("Reading data and converting each data into list_of_list")
    with open(Settings.DATA_PATH + "data.csv", 'r') as csvfile:
        global ids
        dict_reader = list(DictReader(csvfile, delimiter=','))
        ids = list(map(lambda dr: dr['unique_id'], dict_reader))
        return dict_reader


@pytest.fixture(params=get_data(), ids=ids, autouse=False, scope="module")
def get_data_from_csv(request):
    """
    Method to read data from csv file
    Return: list_of_dict
    """
    request.cls.webdriver_path
    print("Data:", request.param)
    return request.param
