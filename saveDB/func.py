from .models import *
from django.db import connection
import sqlite3


def addStudentCourse (num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute('INSERT INTO StudentCourse ("num", "full_name", "topic_selection", "selecting_sources", '
                '"carrying_reserch", "shaping_work", "making", "defending") VALUES (?,?,?,?,?,?,?,?)'
                'RETURNING *', (num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending))
    row = cur.fetchone()
    cur.close()
    connection.commit()

    return dict(row)

def getStudentCourse (num, full_name, topic_selection, selecting_sources,
                  carrying_reserch, shaping_work, making, defending):
    connection = sqlite3.connect("db.sqlite3")
    connection.row_factory = sqlite3.Row
    cur = connection.cursor()
    cur.execute(
        '''SELECT * FROM StudentCourse WHERE "num" LIKE ? AND "full_name" LIKE ? AND "topic_selection" LIKE ?
    AND "selecting_sources" LIKE ? AND "carrying_reserch" LIKE ? AND "shaping_work" LIKE ? AND "making" LIKE ? 
    AND "defending" LIKE ?''', (f"%{num}%", f"%{full_name}%", f"%{topic_selection}%", f"%{selecting_sources}%",
                                f"%{carrying_reserch}%", f"%{shaping_work}%", f"%{making}%", f"%{defending}%"))
    row = cur.fetchall()
    cur.close()
    connection.commit()
    print(row)
    row = [dict(i) for i in row]
    
    return row