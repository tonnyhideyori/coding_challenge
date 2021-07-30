import sqlite3
import time
import datetime
class Database(object):
    #creating data
    def create_data(self,task):
        try:
            conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
            conn.execute('CREATE TABLE messages(urls,content,expire)')
            conn.commit()
        except sqlite3.OperationalError:
            try:
                conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
                conn.execute("CREATE TABLE messages(urls,content,expire)")
                conn.commit()
            except sqlite3.OperationalError:
                print("The table is already created")
        with conn:
            sql='INSERT INTO messages(urls,content,expire) VALUES(?,?,?)'
            conn.execute(sql,task)
            conn.commit()
    
    #retrieveing data
    def access_db(self,unique):
        conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
        sql='SELECT content,expire FROM messages WHERE urls=?;'
        try:
            cur=conn.cursor()
            cur.execute(sql,(unique,))
        except sqlite3.OperationalError:
            cur=conn.cursor()
            cur.execute(sql,(unique,))
        return cur.fetchone()

    #deleting data
    def delete_data(self):
        conn=sqlite3.connect("file::memory:?cache=shared", uri=True)
        sql='DELETE FROM messages WHERE expire = ?;'
        time_diff= time.time() - 7*24*60*60
        cur=conn.cursor()
        cur.execute(sql,(datetime.datetime.fromtimestamp(time_diff).strftime("%Y-%m-%d"),))
        conn.commit()
        