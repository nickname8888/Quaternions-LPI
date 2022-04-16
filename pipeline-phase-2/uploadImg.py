from fileinput import filename
import pyrebase
from datetime import date
import os
from firebase import firebase

config = {
    "apiKey": "AIzaSyC_8KVF3fo25E4hcFX-AEHKY3k0Sl2muII",
  "authDomain": "lip-demo.firebaseapp.com",
  "databaseURL": "https://lip-demo-default-rtdb.firebaseio.com",
  "projectId": "lip-demo",
  "storageBucket": "lip-demo.appspot.com",
  "messagingSenderId": "104538977589",
  "appId": "1:104538977589:web:dbeb64cc44064b4ba0887c",
  "measurementId": "G-XP61FNYFJQ",
  "serviceAccount": "serviceAccountKey.json",
  "databaseURL": "https://lip-demo-default-rtdb.firebaseio.com/"
}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()
auth = firebase.auth()
# path = os.listdir(r"C:\Users\Rishi\Desktop\DEEPBLUE_FINAL\yolov5\runs\detect")
# path.sort()
# print(path)

# print(r"C:\Users\Rishi\Desktop\DEEPBLUE_FINAL\yolov5\runs\detect"+path+r"\crops\license\*")
def uploadimg(path):
  folder = date.today().strftime("%d-%m-%Y")
  rest_path = path[path.find("I"):]
  absPath = r"C:\Users\Rishi\Desktop\DEEPBLUE_FINAL\yolov5\\"
  print(absPath+path)
  storage.child(folder+"/"+rest_path).put(absPath+path)
  return storage.child(folder+"/"+rest_path).get_url(None)


# uploadimg("runs/detect/exp53/crops/license/IMG_7892164.jpg")

# download img
# my_img_path = "lpi-images/IMG_7892.jpg"
# answer = storage.child(my_img_path).put(my_img_path)
# storage.child(my_img_path).download(filename="temp.jpg",path= os.path.basename(my_img_path))

# get url of the image
# users = auth.sign_in_with_email_and_password(email,password)
# url = storage.child(my_img_path).get_url(None)
# print(url)

# uploadimg("runs/detect/exp53/crops/license/IMG_7892164.jpg")