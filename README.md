# Quaternions - License Plate Identification

## Our Goal 

![pipeline diagram](https://www.innominds.com/hs-fs/hubfs/Innominds-201612/img/IM%20Inner%20Pages/ANPR/what-is-anpr.png?width=462&name=what-is-anpr.png)

* The objective is to create a license plate identification system that works in real time. As the population in India keeps growing day by day, so does our traffic. The current solution of Fastag identification is nowhere near fast enough and requires cars to come to a complete stop. 
* Our job here is to implement a working solution that identifies number plates from moving cars, whether they are in different formats or languages, in real-time, such that the cars won’t need to stop and traffic keeps moving.

## Our Approach 
<img src="https://drive.google.com/uc?export=view&id=1Zs-6ryQgT0zWlLSqyqbuHFETK13SqBbY" width="396" height="514">

We start by getting the camera feed for the targeted toll. We use our object detection layer to crop out the Region of Interest - the number plate of the incoming car. We pass that cropped image as input to our OCR layer, which outputs the digits on the plate. If these digits pass the license plate validation, they are logged into the database. In the case where they do not pass the validation test, we pass the image to the second phase of the pipeline, which segments each individual character on the plate, and performs character recognition one by one. After sticking the individual outputs together we pass them on the regex validation once more. If it passes, we log it to the database, if not, the image is passed on to a human operator who then logs it to the database. Now we will quickly move over to the demo. 

## User Interface

Login Screen
<img width="1436" alt="Screenshot 2022-06-10 at 9 42 09 AM" src="https://user-images.githubusercontent.com/61390825/172995849-40a77d3d-3ad7-4224-81c5-8c44028aded2.png">

User Dashboard
<img width="1436" alt="Screenshot 2022-06-10 at 9 41 51 AM" src="https://user-images.githubusercontent.com/61390825/172995897-8ed62948-e6c3-4320-b9d0-f212a56c8460.png">

Marathi Language Support
<img width="1436" alt="Screenshot 2022-06-10 at 9 41 59 AM" src="https://user-images.githubusercontent.com/61390825/172995920-ebaf4882-9e61-485f-a020-6203bc549b94.png">
