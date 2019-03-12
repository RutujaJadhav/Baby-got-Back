from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateEntry, Region
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
import math
import cv2
from PIL import Image
import numpy as np
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

ENDPOINT = "https://southcentralus.api.cognitive.microsoft.com"
prediction_key = "a008d489ab5f4d67baddce65f5cee7e0"
project_id = "07820ee9-2587-417d-acc4-5c1c1bbcf3c3"
iteration_id="3c99bfa5-057f-4d73-9e61-ce4d2f7e84c7"
image_path = "input.jpg"


#infrared
ENDPOINT_i = "https://southcentralus.api.cognitive.microsoft.com"
prediction_key_i = "a008d489ab5f4d67baddce65f5cee7e0"
project_id_i = "ab738f35-2139-498e-becc-2f620f403ed1"
iterationId_i="15239a80-51f2-43ca-b2d7-70f3bb4429ca"


def findDist(p1,p2):
    dist=math.sqrt((p1[0]-p2[0])**2+(p1[1]-p2[1])**2)
    return dist 



thresh=0.3
predictor = CustomVisionPredictionClient(prediction_key, endpoint=ENDPOINT)
predictor_i= CustomVisionPredictionClient(prediction_key_i, endpoint=ENDPOINT_i)

camera = PiCamera()
camera.resolution = (500, 500)

rawCapture = PiRGBArray(camera, size=(500,500))
time.sleep(1)
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    print("cap")
    image = frame.array
    cv2.imwrite("input.jpg",image)
    lab_img=cv2.cvtColor(image,cv2.COLOR_BGR2LAB)
    l_c,a_c,b_c=cv2.split(lab_img)
    if (np.average(l_c))>100: #light threshold
        print ("Daylight")
    
        with open(image_path, mode="rb") as test_data:
            results=predictor.predict_image(project_id, test_data, iteration_id)
        im=np.array(image,dtype=np.uint8)
        res=np.asarray([[p.tag_name,p.probability, p.bounding_box.left, p.bounding_box.top, p.bounding_box.width, p.bounding_box.height] for p in results.predictions])
        classes=res[res[:,1].astype(np.float)>thresh]
	
        print (classes)
        w,h,c=im.shape
        
    else:
        print ("Infrared")    
        with open(image_path, mode="rb") as test_data:
            results=predictor_i.predict_image(project_id_i, test_data, iterationId_i)
        im=np.array(image,dtype=np.uint8)
        res=np.asarray([[p.tag_name,p.probability, p.bounding_box.left, p.bounding_box.top, p.bounding_box.width, p.bounding_box.height] for p in results.predictions])
        classes=res[res[:,1].astype(np.float)>thresh]
	
        print (classes)
        w,h,c=im.shape
    
    obj,obj_loc,highrisk,mediumrisk,lowrisk=[],[],[],[],[]
   
    for cl in classes:
        label=cl[0]+("%.2f" % float(cl[1]))
        obj.append(cl[0]) #array of detected objects

        p1=(int((float(cl[2])*w)),int((float(cl[3])*h)))
        p2=(int(float(cl[2])*w+float(cl[4])*w),int(float(cl[3])*h+float(cl[5])*h))
        center_loc= (int(p1[0]+(p2[0]-p1[0])/2),int(p1[1]+(p2[1]-p1[1])/2))
        obj_loc.append(center_loc)
        if (cl[0]=='Baby'):
            cv2.rectangle(im,p1,p2,(0,255,0),2)
        else: 
            cv2.rectangle(im,p1,p2,(0,0,255),2)
    
        cv2.putText(im,label,p1,cv2.FONT_HERSHEY_SIMPLEX,0.4,(255,255,255),1)
        print (obj)
        print (obj_loc)  
        if 'Baby' in obj:
            
            baby_coords=obj_loc[obj.index('Baby')]
            for objdist in obj_loc:
                d=findDist(baby_coords,objdist)
                if d>0 and d<100:
                    
                    highrisk.append([obj[obj_loc.index(objdist)],int(d)])
                elif d>100 and d<200:
                    mediumrisk.append([obj[obj_loc.index(objdist)],int(d)])
                elif d>200:
                    lowrisk.append([obj[obj_loc.index(objdist)],int(d)])

    print ("highrisk"+ str(highrisk)) ####DISPLAYS OBJECTS CLOSE TO THE BABY AND THE DISTANCE
    print ("mediumrisk"+ str(mediumrisk))
    print ("lowrisk"+ str(lowrisk))
    
    cv2.imwrite("output.jpg",im)
    cv2.imshow("Frame", im)
    
    key = cv2.waitKey(1) & 0xFF

    rawCapture.truncate(0)
    if key == ord("q"):
        break
