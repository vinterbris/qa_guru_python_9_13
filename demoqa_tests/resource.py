import os
import tests

CURRENT_FILE = os.path.abspath(tests.__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
RES_DIR = os.path.join(CURRENT_DIR, os.path.pardir, "resources")


def path(file_name):
    return os.path.abspath(os.path.join(RES_DIR, file_name))
