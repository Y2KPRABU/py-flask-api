import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for)
from drawiofunctions import designer_api

app = Flask(__name__)
app.register_blueprint(designer_api)

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
    

if __name__ == '__main__':
   app.run()
