from database import execute_sql


def create_table():
    # account table
    sql = '''
    CREATE TABLE IF NOT EXISTS account (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
       email TEXT NOT NULL,
       username TEXT NOT NULL,
       password TEXT NOT NULL,
       invitation_code TEXT NOT NULL,
       use_time INT DEFAULT 0,
       can_use_time INT DEFAULT 0,
       is_deleted INT DEFAULT 0,
       create_time DEFAULT (datetime('now', 'localtime'))
    );
    '''
    execute_sql(sql)

create_table()
