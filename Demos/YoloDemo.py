import numpy as np
import cv2 as cv2
whT=320
camp = cv2.VideoCapture(0)
confThreshold = 0.5
classesFile = 'coco.names'
classesNames = []

with open(classesFile, 'rt') as f:
    classesNames = f.read().rstrip('\n').split('\n')

modelConfiguration='yolov3-320.cfg'
modelWeights='yolov3-320.weights'

net=cv2.dnn.readNetFromDarknet(modelConfiguration,darknetModel=modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)

def findObjects(outputs,frame):
    hT,wT,cT=frame.shape
    bbox=[]
    classIds=[]
    confs=[]

    for output in outputs:
        for det in output:
            scores=det[5:]
            classId=np.argmaxs[scores]
            confidence=scores[classId]
            if confidence > confThreshold:
                w,h=int(det[2]*wT),int(det[3]*hT)
                x,y=int((det[0]*wT) -w/2),int((det[1]*hT) -h/2)




while True:

    success, frame = camp.read()
    blob=cv2.dnn.blobFromImage(frame,1/255,(whT,whT),[0,0,0],1,crop=False)
    net.setInput(blob)
    layerNames=net.getLayerNames()
    # print(layerNames)
    outputNames=[layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    outputs=net.forward(outputNames)
    print(outputs)
    cv2.imshow('image', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break

camp.release()
