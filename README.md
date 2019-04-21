# flask-jsDebugger
debug javascript applications in mobiles with flask

### requirements

* python :: tested with python 3.6
* jquery :: tested with 1.12.4
* socket.io :: tested with 1.4.5
* flask
  * flask-socketio
 
### links
python 3.6 : https://www.python.org/downloads/release/python-360/

jquery : https://code.jquery.com

socket.io : https://socket.io/blog/socket-io-1-4-5/
  
### install flask and libraries

`pip install flask`

`pip install flask-socketio`

### debug your files

add the file degugMovile.js in your html code later execute
```javascript

var debugger = DebuggerMovile(true)
debugger.start()

```

if it is passed as argument true will work, if it passes false it will not work as a debugger

### run the server

open the terminal and go to the path where the run.py file is located and run
`python3 run.py` or `python3 /path/to/file/run.py`

### show error

now we just have to wait for the errors to be shown in the terminal and if there is an ajax error they can be seen in the errorAjax folder

### example

open your browser and go to http://127.0.0.1:5000/jsdebug to check that everything works fine, this is an example located in the templates/index.html folder


