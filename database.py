import sqlite3
import time
import datetime
class Database(object):
    def connect(self,task):
        try:
            conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
            conn.execute("create table messages(urls,content,expire)")
            conn.commit()
        except sqlite3.OperationalError:
            try:
                conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
                conn.execute("create table messages(urls,content,expire)")
                conn.commit()
            except sqlite3.OperationalError:
                print("The table is already created")
        try:
            with conn:
                sql='INSERT INTO messages(urls,content,expire) VALUES(?,?,?)'
                conn.execute(sql,task)
                conn.commit()
        except sqlite3.IntegrityError:
            with conn:
                sql='INSERT INTO messages(urls,content,expire) VALUES(?,?,?)'
                conn.execute(sql,task)
                conn.commit()

    def access_db(self,unique):
        conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
        sql='SELECT content,expire FROM messages WHERE urls=?;'
        cur=conn.cursor()
        try:
            cur.execute(sql,(unique,))
        except sqlite3.OperationalError:
            cur.execute(sql,(unique,))
        try:
            cur.execute(sql,(unique,))
        except sqlite3.OperationalError:
            cur.execute(sql,(unique,))

        return cur.fetchone()

    def delete_data(self):
        conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
        sql='DELETE FROM messages WHERE expire = ?;'
        time_diff= time.time() - 8*24*60*60
        cur=self.conn.cursor()
        cur.execute(sql,(datetime.datetime.fromtimestamp(time_diff).strftime("%Y-%m-%d"),))
        conn.commit()
        