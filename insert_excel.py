import sqlite3
from threading import ExceptHookArgs

from xlsxwriter.workbook import Workbook

class Insert():
    def insert_excel(self, chat_id):
        try:
            records = Workbook('records.xlsx')
            worksheet = records.add_worksheet()
            conn=sqlite3.connect('test.db')
            c=conn.cursor()
            mysel=c.execute(f"select * from records where chat_id='{chat_id}'")

            for i, row in enumerate(mysel):
                for j, value in enumerate(row):
                    worksheet.write(i, j, value)
            records.close()

            reports = Workbook('reports.xlsx')
            worksheet = reports.add_worksheet()
            conn=sqlite3.connect('test.db')
            c=conn.cursor()
            mysel=c.execute(f"select * from reports where chat_id='{chat_id}'")

            for i, row in enumerate(mysel):
                for j, value in enumerate(row):
                    worksheet.write(i, j, value)
            reports.close()
            return {'status':'ok'}
        except Exception as ex:
            print(str(ex))