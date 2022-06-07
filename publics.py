from log_tools import log
import os
from consts import consts


def ExceptionLine():
    import linecache
    import sys
    exc_type, exc_obj, tb = sys.exc_info()
    f = tb.tb_frame
    lineno = tb.tb_lineno
    filename = f.f_code.co_filename
    linecache.checkcache(filename)
    line = linecache.getline(filename, lineno, f.f_globals)
    return f"{filename}:{lineno} => {line.strip()}"


def db():
    try:
        from pymongo import MongoClient
        MONGO_CONNECTION = os.getenv('MONGO')
        log.info(f'MONGO_CONNECTION: {MONGO_CONNECTION}')
        if MONGO_CONNECTION is None:
            con = MongoClient(f'mongodb://localhost:{consts.MONGODB_PORT}')
        else:
            con = MongoClient('mongodb://' + MONGO_CONNECTION)
        return con[consts.DB_NAME]
    except:
        log.error(ExceptionLine())
    return None