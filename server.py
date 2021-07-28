from flask import Flask,request,Response
from cryptography.fernet import Fernet
import uuid
from database import Database
import json
import html
import datetime,time,atexit
from apscheduler.schedulers.background import BackgroundScheduler


#loading a key from json file
with open ("key.json") as f:
    key=f.readlines()

#changing a key from string to bytes 
key=json.loads(key[0])['key'].replace("b'","").replace("'","")
fernet =Fernet(key)
app=Flask(__name__)



#home page
@app.route('/',methods=['GET'])
def index():
    return "please enter your message"

#post a message
@app.route("/",methods=['POST'])
def create_message():
    conn=Database()
    #unique url
    unique = uuid.uuid4().hex
    #input sanitazation with html escape
    message = html.escape(request.form['message'])
    #encrpting the message
    encmessage=fernet.encrypt(message.encode())
    url = str(request.base_url)+"message/" + str(unique)
    encunique=fernet.encrypt(unique.encode())
    task = (encunique,encmessage,datetime.datetime.now().strftime("%Y-%m-%d"))
    conn.connect(task)
    print(url)
    return url

@app.route("/message/<url>",methods=["GET"])
def retrive_message(url):
    conn =Database()
    encmessage=conn.access_db(url)
    message=fernet.decrypt(encmessage[0]).decode()
    unique=fernet.decrypt(encmessage[1]).decode()
    return f"your message is: {message}. Created on {unique} "
    #except:
        #return Response("already deleted,page not found",status=404)

@app.route("/delete",methods=["GET"])
def delete_all_data():
    conn =Database()
    conn.delete_data()
    return "all data deleted"
    
#cron for deleting data after 7 days
schedulers=BackgroundScheduler()
schedulers.add_job(func=delete_all_data,trigger="interval",seconds=8*24*60*59)
schedulers.start()
atexit.register(lambda:schedulers.shutdown())

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0", port="5000")