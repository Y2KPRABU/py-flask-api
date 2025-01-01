import drawpyo

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

def Plotobjects(string_array,page):    
        parent_container = drawpyo.diagram.object_from_library(
        library="general", obj_name="labeled_horizontal_container", page=page
            )
        parent_container.autosize_to_children = True
        index = 0
        vertArrayIndex=0
        Lev1Index=0
        Lev2Index=0
        Lev1EntitiesList=[]
        Lev2EntitiesList=[]
        y=200
        x=100
        HorizArrayIndex=0

        for entity in string_array:
            y=200
            if(entity != None and entity != '' and ('|') in entity ):
                Lev2Entities_array = entity.split('|')
                vertArrayIndex=0
                for entity2 in Lev2Entities_array:
                    block_lev2 = drawpyo.diagram.Object(
                    position=(x, y), parent=parent_container, value=entity2, page=page)
                    y=y+200
                    if(vertArrayIndex % 2 ==0 ):   
                        Lev1Index+=1             
                        Lev1EntitiesList.append(block_lev2)
                    else:
                        Lev2Index+=1
                        Lev2EntitiesList.append(block_lev2)
                    vertArrayIndex+=1
                #if(Lev2Index>0 and Lev2Index % 2 !=0 ): #only alternate times the vertical links are created
                Vertlink = drawpyo.diagram.Edge(
                                page=page,source=Lev1EntitiesList[Lev1Index-1],target=Lev2EntitiesList[Lev2Index-1],)
                x=x+200
                if (HorizArrayIndex !=0): #Skip only for the first time
                    Horizlink = drawpyo.diagram.Edge(
                                page=page,source=Lev1EntitiesList[HorizArrayIndex-1],target=Lev1EntitiesList[HorizArrayIndex],)
                HorizArrayIndex+=1
            else:
                block_horiz_without_seps = drawpyo.diagram.Object(
                position=(x, y), parent=parent_container, value=entity, page=page)
                x=x+200
                Lev1EntitiesList.append(block_horiz_without_seps)
                
                if(index>0):
                    link = drawpyo.diagram.Edge(
                    page=page,source=Lev1EntitiesList[index-1],target=Lev1EntitiesList[index],)
                index+=1
           
    
def SaveToFile(file):
    # Write the file
    file.write()

"""Generates a draw.io file with the given entities and saves it to the specified folder path with the specified file name prefix."""
if(__name__ == '__main__'):
    file,page = CreateDrawIoFile()
    EntityListSample = ["Step 1|Step1.1|Step1.2", "Step 2|Step2.1", "Step 3|Step3.1"]
    #EntityListSample = ["Step 1", "Step 2", "Step 3"]

    Plotobjects(EntityListSample,page)
    SaveToFile(file)
    print( 'File Created successfully')