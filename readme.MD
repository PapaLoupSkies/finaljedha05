Project: Fruit and vegetables image Detection and Classification with VGG16 and Yolo V3


  #### Model 1 - Fruit and vegetables image Classification with Transfer Learning using VGG16
    This model is based on the dataset FRUIT-360.
    This dataset contains more than 90,000 images of fruits and vegetables.
    The purpose of this model is to classify images of fruits and vegetables according to their variety : apple, banana, avocado, etc.
    We created this CNN model using transfer learning with the following models : VGG16, ResNet101, InceptionV3 and Xception.

 But this model will not be contained in our web application.  It will be transfered by keras into tflite for our flutter application.


  #### Model 2 - Fruit & vegetables image Detection and Classification with YoloV3
    The purpose of this model is to detect and classify images of fruits and vegetables according to their variety : apple, banana, avocado, etc.
    This model is based on the OpenImage Dataset.
    This dataset contains ~9 million varied images with rich annotations. The images are very diverse and often contain complex scenes with several objects (8.4 per image on average). 
    It contains image-level labels annotations, object bounding boxes, object segmentations,
    visual relationships, localized narratives, and more. 
    We focused on 18 categories of fruits and vegetables images for our Detection model. Those images contain multiple objects and are able to detect if one of those 18 type of fruits or vegetables are represented in the image.
    We created this model using Darknet with YoloV3.
 
 #### Architecture of our project :
   There are two containers managed by docker-compose:
        1. Container with Flask with uWSGI,  so all of python libraries will be build in this container.
        2. Container with NGINX -> our web server for our AWS virtuel machine
   How to use ? 
        Download this folder into your PC or Upload it on your Cloud virtuel machine ,
          in unix, run :  cd server -> chmod +x init.sh -> ./init.sh

 
  ### Authors:
  Haoshi Chen
  Elodie Pointeau
