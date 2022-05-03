from calendar import c
from re import X
import firebase_admin
from datetime import datetime
from firebase_admin import credentials
from firebase_admin import firestore
import pendulum
from datetime import date
cred = credentials.Certificate("../yolov5/utils/serviceAccountKey.json")
ist = pendulum.timezone('Asia/Calcutta')

firebase_admin.initialize_app(cred)
db = firestore.client()

def storePlate(url,op):
    folder = date.today().strftime("%d-%m-%Y")
    time = datetime.now(ist)
    # image_path = folder+"\\"+rest_path
    data = {'location':'Thane','image': url,'plate': op, "time":str(time) }
    print(data)
    db.collection('test4').add(data)
    

