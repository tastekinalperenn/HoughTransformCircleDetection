import numpy as np
import cv2
import math
import matplotlib.pyplot as plt 
import sys  


# With this function I read ground truth files for calculating IoU and determine radius range 
def readGroundTruth(groundTruthFile):
    file = open(groundTruthFile,"r").readlines()
    radiusArray = []
    for i in range (1,len(file)):
        radiusArray.append(file[i].split())
    return radiusArray

# With this funciton I read image and detect edges with using Canny edge detector. After that I return image matrix 
def edgeDetection(imagePath):
    image = cv2.imread(imagePath, 0)
    if(image is not None):
        blur = cv2.GaussianBlur(image,(5,5),0)
        edges = cv2.Canny(image=blur, threshold1=50, threshold2=250) # Canny Edge Detection
        imageMatrix = np.array(edges)
        return imageMatrix
    else:
        return []

# Here I implement Hough transform. 
def houghtransform(a,b,radius,counter):
    radius = int(float(radius))
    # I create angle array for voting canidate circles 
    angles = np.arange(start = 0, stop = 360,step = 5,dtype = int) # Our step is 5.If we choose 1 then we get more accuracy but a bit slow performance
    for i in angles:
        # Here calculate center points of circle based on radius and pixel coordinate. Every pixel of image corresponds to a circle
        x = round (a + radius*math.cos(math.radians(i)))
        y = round (b + radius*math.sin(math.radians(i)))
        # With these two step I vote circle center coordinates
        if((x,y) in counter.keys()):
            counter[(x,y)] = counter[(x,y)] +1
        else :
            counter[(x,y)] = 1

# With this function I draw all of detected circles on input image then show this output image
def drawCircle(image,circleCenters):
    for circle in circleCenters:
        image = cv2.circle(image, circle[0], circle[1], (255,0,0), 2)
    cv2.imshow("Detected Circles",outputImage)
    cv2.imwrite("Output"+str(sys.argv[1]),outputImage)
    cv2.waitKey(0)
    
# I use this function for calculate distance between two circle
def calculateCenterDistances(x0,y0,x1,y1):
    return math.sqrt((x0-x1)**2 + (y0-y1)**2)

      
    

imageMatrix = edgeDetection(str(sys.argv[1]))
outputImage = cv2.imread(str(sys.argv[1]))

if(len(imageMatrix)==0):
    print("Error : Image cannot open!")
else:
    # With this I get array which is contain white pixels(edge pixels)
    xAxis, yAxis = np.where(imageMatrix==255)
    groundTruth = readGroundTruth(str(sys.argv[2]))
   
    # I will store all of detected circles in this arrray.
    circleCenters = []
    circleCount = len(groundTruth)
    for j in range(circleCount): # I try to detect circle count as specified in the ground truth file
        counter = {} # I use this for voting circle center
        for i in range(len(xAxis)):
            houghtransform(xAxis[i], yAxis[i],groundTruth[j][2],counter)
        
        # Here voting operations finished. I get most voted 30 center candidates because sometimes more than one coordinate 
        # has same vote count. 
        mostVotedPoints = []
        for i in range(30):
            mostVotedPoints.append(max(counter, key=counter.get))
            del counter[max(counter, key=counter.get)]     
        # After get most voted 30 center candidate I calculate distance between ground truth and get min distances center point.
        mostVotedPointsIoU = {}
        for i in mostVotedPoints:
            mostVotedPointsIoU[i] = calculateCenterDistances(i[1], i[0] ,int(float(groundTruth[j][0])), int(float(groundTruth[j][1])))
        # Select minumum distances center point corresponding to ground truth
        minimum = min(mostVotedPointsIoU, key=mostVotedPointsIoU.get)
        circleCenters.append(((minimum[1],minimum[0]), int(float(groundTruth[j][2]))))
    
    drawCircle(outputImage,circleCenters)
    





    
