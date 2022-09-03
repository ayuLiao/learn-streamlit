from database import *


class AccountModel:

    @staticmethod
    def get_all_accounts():
        sql = '''
        SELECT * FROM accounts WHERE is_deleted=0
        '''
        return query_sql(sql)

    @staticmethod
    def get_account(username):
        sql = f'''
        SELECT * FROM account WHERE username = '{username}' AND is_deleted=0
        '''
        return query_sql(sql)

    @staticmethod
    def add_account(email, username, password, invitation_code, use_time, can_use_time):
        sql = f'''
        INSERT INTO account (
            email,
            username,
            password,
            invitation_code,
            use_time,
            can_use_time
        ) VALUES (
            '{email}',
            '{username}',
            '{password}',
            '{invitation_code}',
            {use_time},
            {can_use_time}
        )
        '''
        return insert_sql(sql)
