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
        EntitiesList=[]
        y=200
        x=100
        for entity in string_array:
            block_a = drawpyo.diagram.Object(
            position=(x, y), parent=parent_container, value=entity, page=page)
            x=x+200
            EntitiesList.append(block_a)
            
            if(index>0):
                link = drawpyo.diagram.Edge(
                page=page,source=EntitiesList[index-1],target=EntitiesList[index],)
            index+=1
    #parent_container.add_object(block_1)
    #parent_container.add_object(block_2)

    
def SaveToFile(file):
    # Write the file
    file.write()

"""Generates a draw.io file with the given entities and saves it to the specified folder path with the specified file name prefix."""
if(__name__ == '__main__'):
    file,page = CreateDrawIoFile()
    EntityListSample = ["Step 1|Step1.1", "Step 2|Step2.1", "Step 3|Step3.1"]

    Plotobjects(EntityListSample,page)
    SaveToFile(file)
    print( 'File Created successfully')