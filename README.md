# Quaternions - License Plate Identification

## Our Goal 

![pipeline diagram](https://www.researchgate.net/profile/Zain-Masood-4/publication/315489495/figure/fig3/AS:900203120967681@1591636557193/Figure-shows-some-results-of-our-end-to-end-license-plate-detection-and-recognition.png)

* The objective is to create a license plate identification system that works in real time. As the population in India keeps growing day by day, so does our traffic. The current solution of Fastag identification is nowhere near fast enough and requires cars to come to a complete stop. 
* Our job here is to implement a working solution that identifies number plates from moving cars, whether they are in different formats or languages, in real-time, such that the cars won’t need to stop and traffic keeps moving.

## Our Approach 
<img src="https://drive.google.com/uc?export=view&id=1Zs-6ryQgT0zWlLSqyqbuHFETK13SqBbY" width="396" height="514">

We start by getting the camera feed for the targeted toll. We use our object detection layer to crop out the Region of Interest - the number plate of the incoming car. We pass that cropped image as input to our OCR layer, which outputs the digits on the plate. If these digits pass the license plate validation, they are logged into the database. In the case where they do not pass the validation test, we pass the image to the second phase of the pipeline, which segments each individual character on the plate, and performs character recognition one by one. After sticking the individual outputs together we pass them on the regex validation once more. If it passes, we log it to the database, if not, the image is passed on to a human operator who then logs it to the database. Now we will quickly move over to the demo. 



