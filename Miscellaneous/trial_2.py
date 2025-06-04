##Date : 11-5-24
##modified real time image in curret ERP  modified and working
from frappe_client.frappeclient import FrappeClient
from frappe_client import auth
import subprocess
import shlex
from datetime import datetime
#import serial as ser
import time

sleep_time_s =60
product_group = "Product-Capvel VAT"
command = '<A,SAMPLE>'
session_descripton  = "Testing new firmware version 1.0"
baud_rate = 9600
session_id =  "IS-00027" #if set to none, a new session is created
print_output = False



def create_session(product_group,client,session_id,description = "Test Log"):
    session_doc = { "doctype":"IOT Session",
                    "product":product_group,
                    "start_time": datetime.now().strftime("%Y-%m-%d %H:%H:%S"),
                    "description":description
                 }
    try:
        return client.insert(session_doc)
    except:
        logging.info("Could not create session")
        return None

def get_session(session_id,client):
    session = None
    try:
        session =  client.get_doc("IOT Session",session_id)
        return session
    except:
        logging.info("No session by the given name")
        return None

def insert_log(client,session,data):
    response = client.insert({"doctype":"IOT Raw Log",
                          "data":data,#.replace('\t',',').replace(':','-').replace('<','').replace('>',''),
                          "data":"'" + data + "'",

                          "timestamp":datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          "iot_session":session
                   })
    return response
client = FrappeClient(auth.url, api_key = auth.api_key, api_secret = auth.api_secret)
session_doc = get_session(session_id, client)
if session_doc == None or "name" not in session_doc:
    session_doc = create_session(product_group, client,session_id, session_descripton)


output = insert_log(client,session_doc["name"],"new")

'''
res = client.get_doc("IOT Session","IS-00027")
print(res)
session_id = "IS-00027"
res1 = get_session(session_id,client)
print(res1)
'''

res = client.get_list("IOT Raw Log",filters = {"iot_session":"IS-00027","timestamp":["=",datetime.now().strftime("%Y-%m-%d %H:%H:%S")]},order_by="timestamp")
print(res)
print(len(res))

subprocess.run(shlex.split("./file_upload.sh " + res[-1]["name"] ))



