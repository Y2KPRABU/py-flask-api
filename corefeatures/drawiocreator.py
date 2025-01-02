import drawpyo
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