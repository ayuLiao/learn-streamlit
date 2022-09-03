import os
import sqlite3
from configs import ROOT_PATH

sqlite_db_path = os.path.join(ROOT_PATH, 'hello.db')


def execute_sql(sql):
    conn = sqlite3.connect(sqlite_db_path)
    with conn:
        conn.execute(sql)


def insert_sql(sql):
    conn = sqlite3.connect(sqlite_db_path)
    with conn:
        result = conn.execute(sql)
    return result.lastrowid


def query_sql(sql):
    """
    return -> List(dict)
    """
    conn = sqlite3.connect(sqlite_db_path)
    conn.row_factory = sqlite3.Row
    with conn:
        datas = conn.execute(sql)
        # sqlite3 row object => list[dict]
        row_datas = [dict(zip(data.keys(), data)) for data in datas]
    return row_datas
