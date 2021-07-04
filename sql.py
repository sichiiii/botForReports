from sqlalchemy import create_engine
from sqlalchemy import *
from sqlalchemy import Table, Column, Integer, String, MetaData


class SQLITE:
    def __init__(self):
        self.engine = create_engine('sqlite:///test.db')
        self.meta = MetaData(self.engine)

    def addRecord(self, id, name, time, chat_id):
        records = Table('records', self.meta, Column('id', Integer), \
            Column('name', String),  Column('time', String), \
                Column('chat_id', Integer), extend_existing=True)
        self.meta.create_all(self.engine)
        try:
            with self.engine.connect() as con:
                stm = insert(records).values(id=id, name=name, time=time, chat_id=chat_id)
                rs = con.execute(stm)
                return {'status':'ok'}
        except Exception as ex:
            print(ex)

    def addReport(self, id, name, money, time, chat_id):
        reports = Table('reports', self.meta, Column('id', Integer), \
            Column('name', String), Column('money', String), \
                Column('time', String), Column('chat_id', Integer), extend_existing=True)
        self.meta.create_all(self.engine)
        try:
            with self.engine.connect() as con:
                stm = insert(reports).values(id=id, name=name, money=money, time=time, chat_id=chat_id)
                rs = con.execute(stm)
                return {'status':'ok'}
        except Exception as ex:
            print(ex)
        