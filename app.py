import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for,make_response, send_file)

app = Flask(__name__)
#Constants for Application
GenFile_FolderPath='.\\'
GenFile_Name_Prefix ='generated_diagram2.drawio'

@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST','GET'])
def hello():
   name = request.form.get('name')

   if name:
       print('Request for hello page received with name=%s' % name)
       return render_template('hello.html', name = name)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       return redirect(url_for('index'))

@app.route('/hello2', methods=['GET'])
def hello2():
       print('Request for hello page received with no name or blank name -- redirecting')
       return 'hello sundar'
import drawpyo

def CreateDrawIoFile():
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
        y=300
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

@app.route('/createdrawio', methods=['GET'])    
def ConvertStringsToImage():
    strEntities = request.args.get('name')
    EntityList =[]
    if(strEntities != None):
        EntityList = strEntities.split(',')
    else:
        EntityList = ["Step 1", "Step 2", "Step 3"]
    file,page = CreateDrawIoFile()
    Plotobjects(EntityList,page)
    SaveToFile(file)
    print( 'File Created successfully')
    file_path = os.path.join(GenFile_FolderPath, GenFile_Name_Prefix)
    return return_fileto_download(file_path)

def return_fileto_download(filename,asattachment=True):
    try:
        #filename = secure_filename(filename)  # Sanitize the filename
        #file_path = os.path.join(GenFile_FolderPath, filename)
        if os.path.isfile(filename):
            return send_file(filename, as_attachment=asattachment,
                mimetype='application/pdf',download_name='GenDesignDoc.drawio')
        else:
            return make_response(f"File '{filename}' not found.", 404)
    except Exception as e:
        return make_response(f"Error: {str(e)}", 405)
    

if __name__ == '__main__':
   app.run()
