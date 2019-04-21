from flask import Flask,render_template,jsonify
from flask_socketio import SocketIO
from datetime import datetime
import re

app = Flask(__name__,template_folder='templates',static_url_path='/static',static_folder='static')
socket = SocketIO(app)

def saveAjaxError(responseText):
    nameFile = datetime.now().strftime('%d-%m-%Y %H-%M-%S.text')
    fullPath = 'errorAjax/{}'.format(nameFile)
    search = re.search(r'</html>(.*)',responseText,re.DOTALL | re.MULTILINE)
    try:
        traceback = search.group(1).strip()
    except:
        traceback = responseText

    f = open(fullPath,'w')
    f.write(traceback)
    f.close()

@app.route('/test')
def test():
    return jsonify(status='success')

@app.route('/testerror')
def testerror():
    return a*b

@app.route('/jsdebug')
def jsdebug():
    return render_template('index.html')

@socket.on('debugError',namespace='/debugger')
def error(errors):
    print(errors)

@socket.on('debugAjax',namespace='/debugger')
def errorAjax(errors):
    errorAjax = errors['responseText']
    del errors['responseText']
    saveAjaxError(errorAjax)
    print(errors)

if __name__ == '__main__':
    socket.run(app,debug=True)