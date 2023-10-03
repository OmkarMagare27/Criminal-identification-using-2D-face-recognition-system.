import os
import cv2
import numpy as np 
from PIL import Image
#recognizer = cv2.createLBPHFaceRecognizer()
from tkinter import messagebox

recognizer = cv2.face.LBPHFaceRecognizer_create()
path = 'dataset'
if not os.path.exists('./recognizer'):
    os.makedirs('./recognizer')
def getImagesWithID():
  imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
  print(imagePaths)
  faces = []
  IDs = []
  for imagePath in imagePaths:
    faceImg = Image.open(imagePath).convert('L')
    faceNp = np.array(faceImg,'uint8')
    print(os.path.split(imagePath)[-1].split('.')[2])
    ID = int(os.path.split(imagePath)[-1].split('.')[2])
    faces.append(faceNp)
    IDs.append(ID)
    cv2.imshow("training",faceNp)
    cv2.waitKey(10)
  return np.array(IDs), faces
def train1():
    Ids, faces = getImagesWithID()
    recognizer.train(faces,Ids)
    recognizer.save('recognizer/trainingData.yml')
    messagebox.showinfo("Information", "Training Completed.")
    cv2.destroyAllWindows()
