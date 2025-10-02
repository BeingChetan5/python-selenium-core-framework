import os


class Settings(object):
    ROOT_PATH = os.path.realpath(os.path.join(os.path.dirname(__file__), '.'))
    DATA_PATH = ROOT_PATH + "/tools/test_data/"
    driver_path = ""
