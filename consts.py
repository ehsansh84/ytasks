import os


class consts(object):
    PROJECT_NAME = 'ytasks'
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    MONGODB_PORT = '27017'
    DB_NAME = PROJECT_NAME if os.getenv('DB_NAME') is None else os.getenv('DB_NAME')
