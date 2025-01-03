import cv2
import drawpyo

# Load the image
image = cv2.imread("D:\lsegwork\OneDrive - London Stock Exchange Group\wealthnTrade\Proposals Conceptual View.jpg", cv2.IMREAD_GRAYSCALE)

# Detect edges
edges = cv2.Canny(image, 100, 200)

# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
def CreateDrawIoFile():
    # Create a new draw.io file
    file = drawpyo.File()
    file.file_path = 'D:\\lsegwork\\'
    file.file_name = 'generated_diagram.drawio'

    # Add a page
    page = drawpyo.Page(file=file)
    return file,page
def AddObjects(page,contours):    
    # Iterate over contours and add them to the draw.io diagram
    intCtr=0
    for contour in contours:
        intCtr= intCtr+1
        x, y, w, h = cv2.boundingRect(contour)
        obj = drawpyo.diagram.Object(page=page, value=str(intCtr))
        obj.position = (x, y)
        obj.width = w
        obj.height = h
def AddLines(page,lines):    
    # Iterate over contours and add them to the draw.io diagram
    intCtr=0
    for eachline in lines:
        intCtr= intCtr+1
        #if(intCtr > 60):
        #    break
        for x1, y1, x2, y2 in eachline:
            obj1 = drawpyo.diagram.Object(page=page, value='')
            obj1.position = x1,y1
            obj1.width=1
            obj1.height=1
            obj2 = drawpyo.diagram.Object(page=page, value='')
            obj2.position = x2,y2
            obj2.width=1
            obj2.height=1
           
            link = drawpyo.diagram.Edge(page=page,source=obj1,
    target=obj2)
            """ if x1 == x2:  # Vertical line
                obj.position = (x1, y1)
                obj.width = 2
                obj.height = y2-y1
            elif y1==y2: # horizontal line
                obj.position = (x1, y1)
                obj.width = x2-x1
                obj.height = 2
"""
def SaveToFile(file):
    # Write the file
    file.write()
#file,page = CreateDrawIoFile()
#AddObjects(page,contours)
#SaveToFile(file)


