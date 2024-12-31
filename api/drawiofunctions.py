import os

from flask import Blueprint
from flask import (request,make_response, send_file)
from corefeatures.drawiocreator import CreateDrawIoFile,Plotobjects,SaveToFile

# Constants for Application
GenFile_FolderPath='.\\'
GenFile_Name_Prefix ='generated_diagram2.drawio'


designer_api = Blueprint('designer_api', __name__)
@designer_api.route("/api/designer")
def hello():
    return "list of drawio apis are here"   


@designer_api.route('/api/createdrawio', methods=['GET'])    
def ConvertStringsToImage():
    strEntities = request.args.get('name')
    EntityList =[]
    if(strEntities != None):
        EntityList = strEntities.split(',')
    else:
        EntityList = ["Step 1|Step1.1", "Step 2|Step2.1", "Step 3|Step3.1"]
    file,page = CreateDrawIoFile()
    Plotobjects(EntityList,page)
    SaveToFile(file)
    print( 'File Created successfully')
    file_path = os.path.join(GenFile_FolderPath, GenFile_Name_Prefix)
    return return_fileto_download(file_path)

"""Returns the file to download in a HTTP Response format from a given file path."""
def return_fileto_download(filePath,asattachment=True):
    try:
        #filename = secure_filename(filename)  # Sanitize the filename
        #file_path = os.path.join(GenFile_FolderPath, filename)
        if os.path.isfile(filePath):
            return send_file(filePath, as_attachment=asattachment,
                mimetype='application/pdf',download_name='GenDesignDoc.drawio')
        else:
            return make_response(f"File '{filePath}' not found.", 404)
    except Exception as e:
        return make_response(f"Error: {str(e)}", 405)

