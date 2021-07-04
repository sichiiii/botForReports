import sqlite3

from xlsxwriter.workbook import Workbook

records = Workbook('records.xlsx')
worksheet = records.add_worksheet()
conn=sqlite3.connect('test.db')
c=conn.cursor()
mysel=c.execute("select * from records")

for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)
records.close()

reports = Workbook('reports.xlsx')
worksheet = reports.add_worksheet()
conn=sqlite3.connect('test.db')
c=conn.cursor()
mysel=c.execute("select * from reports")

for i, row in enumerate(mysel):
    for j, value in enumerate(row):
        worksheet.write(i, j, value)
reports.close()