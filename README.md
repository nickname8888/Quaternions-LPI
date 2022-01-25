# Quaternions - License Plate Identification

## Our Goal 

![pipeline diagram](https://www.researchgate.net/profile/Zain-Masood-4/publication/315489495/figure/fig3/AS:900203120967681@1591636557193/Figure-shows-some-results-of-our-end-to-end-license-plate-detection-and-recognition.png)

* The objective is to create a license plate identification system that works in real time. As the population in India keeps growing day by day, so does our traffic. The current solution of Fastag identification is nowhere near fast enough and requires cars to come to a complete stop. 
* Our job here is to implement a working solution that identifies number plates from moving cars, whether they are in different formats or languages, in real-time, such that the cars won’t need to stop and traffic keeps moving.

## Our Approach 

![image](https://drive.google.com/uc?export=view&id=1RVbbK0uoBTfqqiDT_CEl-I1SyS-DjGXq)

* Our approach is to build 3 different layers and then merge them seamlessly, the 3 layers being object detection, language prediction, and OCR (which will be different for each language) layers. 
* We would have our entire pipeline run on the cloud so as to reduce processing on the client-side, such that the user's computer will only handle the camera's input streams while the rest of the processing is done on the cloud. 
* Accounting for internet instability/outages, we will also provide an offline solution for the same pipeline.
