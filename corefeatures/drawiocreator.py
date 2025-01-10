import drawpyo
import cv2
from stringsplitter import split_string 
# Constants for Application

"""Generates a draw.io file with the given entities and saves it to the specified folder path with the specified file name prefix."""
def CreateDrawIoFile(GenFile_FolderPath='.',
GenFile_Name_Prefix ='generated_diagram2.drawio'):
    # Create a new draw.io file
    file = drawpyo.File()
    file.file_path = GenFile_FolderPath
    file.file_name = GenFile_Name_Prefix

    # Add a page
    page = drawpyo.Page(file=file)
    return file,page

""" function to add Container to the draw.io diagram     """
def AddContainer(page):
    parent_container = drawpyo.diagram.object_from_library(
        library="general", obj_name="labeled_horizontal_container", page=page
    )
    parent_container.autosize_to_children = True

    block_1 = drawpyo.diagram.object_from_library(
        library="general", obj_name="rectangle", page=page
    )
    block_1.value = "Block 1"
    block_1.parent = parent_container
    block_1.position= (100,300)

    block_2 = drawpyo.diagram.Object(
        position=(300, 300), parent=parent_container, value="Block 2", page=page)
    link = drawpyo.diagram.Edge(
    page=page,
    source=block_1,
    target=block_2,
    )
""" function to Plot a connected object from a comma sep string 
to the draw.io diagram     """
def Plotobjects(InputString_WithSeps,page):    
        parent_container = drawpyo.diagram.object_from_library(
        library="general", obj_name="labeled_horizontal_container", page=page
            )
        parent_container.autosize_to_children = True
        Lev1EntitiesList=[]
        HorizDrawObjectsList=[]
        VertDrawObjectsList=[]
        TwoDimArrayResult=[]
        y=200
        x=100
        HorizArrayIndex=0
        TwoDimArrayResult,Lev1EntitiesList =  split_string( InputString_WithSeps)
        #Build the horizontal entities first
        for entity in Lev1EntitiesList:
            y=200
            if(entity != None and entity != ''):
                
                horizblock = drawpyo.diagram.Object(
                position=(x, y), parent=parent_container, value=entity, page=page)
                x=x+200
                HorizDrawObjectsList.append(horizblock)
                if (HorizArrayIndex !=0): #Skip only for the first time
                    Horizlink = drawpyo.diagram.Edge(
                                page=page,source=HorizDrawObjectsList[HorizArrayIndex-1],target=HorizDrawObjectsList[HorizArrayIndex],)
                HorizArrayIndex+=1

        #Print the vertical entities
        vertArrayIndex=0
        x=100
        for sub_array in TwoDimArrayResult:
            if(sub_array != None and (len(sub_array) != 0)):
                vertArrayIndex=0
                VertDrawObjectsList.clear()
                y=200
                for entity in sub_array:
                    if(entity != None and entity != ''):
                        vertblock = drawpyo.diagram.Object(
                            position=(x, y), parent=parent_container, value=entity, page=page)
                        y=y+200
                        VertDrawObjectsList.append(vertblock)
                        if (vertArrayIndex !=0): #Skip only for the first time
                            Vertlink = drawpyo.diagram.Edge(
                                page=page,source=VertDrawObjectsList[vertArrayIndex-1],target=VertDrawObjectsList[vertArrayIndex],)
                    vertArrayIndex+=1
            x=x+200
""" function to add lines to the draw.io diagram     """        
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
           
            link = drawpyo.diagram.Edge(page=page,source=obj2,
    target=obj1)
            """ if x1 == x2:  # Vertical line
                obj.position = (x1, y1)
                obj.width = 2
                obj.height = y2-y1
            elif y1==y2: # horizontal line
                obj.position = (x1, y1)
                obj.width = x2-x1
                obj.height = 2
"""

""" function to add objects to the draw.io diagram     """
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

""" function to save the draw.io file     """   
def SaveToFile(file):
    # Write the file
    file.write()

"""Generates a draw.io file with the given entities and saves it to the specified folder path with the specified file name prefix."""
if(__name__ == '__main__'):
    file,page = CreateDrawIoFile()
    EntityListSample = "Step 1|Step1.1|Step1.2, Step 2|Step2.1 ,Step 3|Step3.1"
    #EntityListSample = ["Step 1", "Step 2", "Step 3"]

    Plotobjects(EntityListSample,page)
    SaveToFile(file)
    print( 'File Created successfully')