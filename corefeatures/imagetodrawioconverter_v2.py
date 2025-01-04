import cv2 
import numpy as np 
from matplotlib import pyplot as plt 
from drawiocreator import *
import os

#pathtoSrcImg = 'D:\lsegwork\OneDrive - London Stock Exchange Group\wealthnTrade\Proposals Conceptual View.jpg'
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# Define the subfolder name
samplesrcfile = 'static/images/sample_steps_diagram.jpg'
print(parent_dir)
# Construct the full path to the subfolder
pathtoSrcImg = os.path.join(parent_dir, samplesrcfile)
print(pathtoSrcImg)
if(os.path.isfile(pathtoSrcImg)==False):
    print('File does not exist')
    exit(0) 
# Print the subfolder path
print(pathtoSrcImg)

imgWithSquares = ''
def plot_all_images(pathtoSrc):  
    # reading image 
    img = cv2.imread(pathtoSrc) 
    
    # converting image into grayscale image 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
    
    # setting threshold of gray image 
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) 
    
    # using a findContours() function 
    contours, _ = cv2.findContours( 
        threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) 
    
    i = 0
    print('No of contours : ' + str(len(contours)))
    ctr=0
    # list for storing names of shapes 
    for contour in contours: 
    
        # here we are ignoring first counter because  
        # findcontour function detects whole image as shape 
        if i == 0: 
            i = 1
            continue
    
        # cv2.approxPloyDP() function to approximate the shape 
        approx = cv2.approxPolyDP( 
            contour, 0.01 * cv2.arcLength(contour, True), True) 
        if(len(approx)>10):
            continue 
        ctr=ctr+1
    
        # using drawContours() function 
        cv2.drawContours(img, [contour], 0, (0, 0, 255), 1) 

        # finding center point of shape 
        M = cv2.moments(contour) 
        if M['m00'] != 0.0: 
            x = int(M['m10']/M['m00']) 
            y = int(M['m01']/M['m00']) 
    
        # putting shape name at center of each shape 
        if len(approx) == 3: 
            cv2.putText(img, 'Triangle', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2) 
    
        elif len(approx) == 4: 
            cv2.putText(img, 'Rect', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2) 
    
        elif len(approx) == 5: 
            cv2.putText(img, '', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
        elif len(approx) == 6: 
            cv2.putText(img, '', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
        else: 
            cv2.putText(img, '', (x, y), 
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2) 
    
    # displaying the image after drawing contours 
    print('No of contours drawn: ' + str(ctr))

    cv2.imshow('converted shapes', img) 
    
    cv2.waitKey(0) 
    cv2.destroyAllWindows() 

def detect_big_shapes(image_path, min_area=100):
    # Load the image
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Detect edges in the image
    edged = cv2.Canny(gray, 50, 150)
    
    # Find contours in the edged image
    contours, _ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Loop over the contours
    for contour in contours:
        # If the contour is not sufficiently large, ignore it
        if cv2.contourArea(contour) < min_area:
            continue
        
        # Approximate the contour
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.02 * peri, True)
        
        # If the contour has closed edges (is a closed shape), draw it on the image
        if len(approx) >= 3:
            cv2.drawContours(image, [approx], -1, (0, 255, 0), 1)
    
    # Show the output image
    cv2.imshow("Detected Shapes", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Option 3 to plot edges only
def plot_Edges(pathtoSrc):
    img = cv2.imread(pathtoSrc, cv2.IMREAD_GRAYSCALE)

    # Apply Canny edge detection
    edges = cv2.Canny(img, 100, 200)

    # Display the original and edge-detected images
    plt.subplot(121), plt.imshow(img, cmap='gray')
    plt.title('Original Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(edges, cmap='gray')
    plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
    plt.show()
# Example usage
def DetectLines(pathtoSrcImg):
    import numpy as np
    import matplotlib.pyplot as plt
    import cv2
    import sys

    # read the image from arguments
    image = cv2.imread(pathtoSrcImg)

    # convert to grayscale
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # perform edge detection
    edges = cv2.Canny(grayscale, 30, 100)

    # detect lines in the image using hough lines technique
    lines = cv2.HoughLinesP(edges, 1, np.pi/180, 60, np.array([]), 50, 5)
    print('Detected lines : ' + str(len(lines)))

    # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color=(20, 220, 20), thickness=3)

    # show the image
    plt.imshow(image)
    plt.show()
    return lines
def detect_squares(pathtosrc,min_area=300):
    import cv2
    import numpy as np

    # Load the image
    imgWithSquares = cv2.imread(pathtosrc)
    gray = cv2.cvtColor(imgWithSquares, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find contours
    cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    sqContours=[]
    ctr=0
    print('Init squares : ' + str(len(sqContours)))
    # Filter for squares
    for c in cnts:
        if cv2.contourArea(c) < min_area:
            continue
        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, 0.04 * peri, True)
        if len(approx) == 4:
            #highlight squares with Red colour
            cv2.drawContours(imgWithSquares, [approx], -1, (0, 0, 255), 6)
            ctr=ctr+1
            vertexCtr=0
            #print("Vertices:",approx)
            sqContours.append(approx)
    # Display the image with detected squares
    print('Detected squares' + str(len(sqContours)) + 'ctr: ' +str(ctr))
    print('Vertex counters : ' + str(vertexCtr))

    cv2.imshow('Detected Squares', imgWithSquares)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return sqContours, imgWithSquares
#Merges parallel lines based on threshold value
def merge_lines(lines, threshold=50):
    merged_lines = []
    for line in lines:
        x1, y1, x2, y2 = line[0]
        merged = False
        for merged_line in merged_lines:
            mx1, my1, mx2, my2 = merged_line[0]
            if abs(x1 - mx1) < threshold and abs(y1 - my1) < threshold and abs(x2 - mx2) < threshold and abs(y2 - my2) < threshold:
                merged = True
                break
            if abs(x1 - mx2) < threshold and abs(y1 - my2) < threshold and abs(x2 - mx1) < threshold and abs(y2 - my1) < threshold:
                merged = True
                break

        if not merged:
            merged_lines.append(line)
    return merged_lines

# Function to merge lines
def merge_vertical_lines(lines):
    if len(lines) < 2:
        return lines

    # Sort lines by their x1 coordinate
    lines = sorted(lines, key=lambda line: line[0][0])

    merged_lines=[]
    unmerged_lines = []
    current_line = lines[0]

    for next_line in lines[1:]:
        # Check if lines touch or overlap
        if (current_line[0][2] == next_line[0][0]) or ((next_line[0][0] -current_line[0][2]  ) < 10) :
            # Merge lines by taking the min x1, y1 and max x2, y2
            current_line = [[min(current_line[0][0], next_line[0][0]),
                             min(current_line[0][1], next_line[0][1]),
                             max(current_line[0][2], next_line[0][2]),
                             max(current_line[0][3], next_line[0][3])]]
            merged_lines.append(current_line)
        else:
            unmerged_lines.append(current_line)
        current_line = next_line

    merged_lines.append(unmerged_lines)
    return merged_lines

def LoadShapesAndLinesInDiffColours(pathToSrc):
    # Load the image
    image = cv2.imread(pathToSrc)
 # Load the image
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Find contours
    cnts, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    shapeContoursList=[]
    # Draw contours on the original image
    intCtr=0
    for contour in cnts:
        intCtr=intCtr+1
        if(intCtr ==1):# skip the first image which is the outer box
            continue
        # Approximate the contour to a polygon
        epsilon = 0.09 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

        # If the approximated contour has 3 or 4 points, it is a rectangle, 
        # so  drawing over the shapes in white font color 255,255,255
        if ((len(approx) >= 3) and (cv2.contourArea(approx) >300)):
            shapeContoursList.append(approx)
            cv2.drawContours(image, [approx], -1, (255, 255, 255), 7)
        #elif ((len(approx) <= 4) and (cv2.contourArea(approx) >100)):
            # Draw lines for other shapes in Red
            #cv2.drawContours(image, [approx], -1, (0, 0, 255), 2)
        #else:
            # Draw lines for other shapes
            #cv2.drawContours(image, [approx], -1, (255, 0, 0), 2)   
    print('Detected Shape contours count : ', len(shapeContoursList))
    cv2.imshow('Initial Shapes and Lines with Shapes blurred in white', image)
    cv2.waitKey(0)    
    
    # perform edge detection on image with shapes blurred in white
    # above , not the original image
    # apertureSize=  range between 3 and 7 are the most common values
    #increasing the threshold2 parameter reduces the number of edges detected
    edges = cv2.Canny(image, 20,  threshold2=100, apertureSize=3)

    # detect lines in the image using hough lines technique
    #Increasing rho increases the number of lines detected
    #Increasing threshold decreases the number of lines detected
    #Increasing the theta , by reducing the pi's denominator, reduces the number of lines detected
    #Increasing minLineLength increases the number of lines detected
    #Increasing maxLineGap increases the number of lines
    lines = cv2.HoughLinesP(image=edges, rho=0.5, theta=  np.pi/50, threshold= 70,lines= np.array([]), 
                            minLineLength= 30, maxLineGap=30)
    print('Initial Detected lines : ' + str(len(lines)))

      # iterate over the output lines and draw them
    for line in lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color=(220, 0, 20), thickness=2)
    
    cv2.imshow('Initial  lines blue 1', image)
    cv2.waitKey(0)
    
    filteredLines=merge_lines(lines)
    print('Filtered n merged lines : ' + str(len(filteredLines)))
    joined_lines=(filteredLines)
    #print('Filtered n merged lines : ' + str(len(filteredLines)))
    #print('Joined lines : ' + str(len(joined_lines)))

  
    for line in joined_lines:
        for x1, y1, x2, y2 in line:
            cv2.line(image, (x1, y1), (x2, y2), color=(2, 222, 222), thickness=1)
            #cv2.line(image, (line[0], line[1]), (line[2], line[3]), color=(220, 220, 20), thickness=1)
   
    
  
    cv2.imshow('Lines redrawn  removed', image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return shapeContoursList, joined_lines
# Example usage:
#line = ((2, 3), (2, 7))
#square = ((1, 4), (5, 4))

#diFile, diPage= CreateDrawIoFile()
shapeContours, linesList = LoadShapesAndLinesInDiffColours(pathtoSrcImg)
#AddObjects(diPage,shapeContours)
#AddLines(diPage,linesList)
#SaveToFile(diFile)
print('File Created successfully')

