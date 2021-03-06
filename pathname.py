from flask import Flask
from flask import jsonify
from flask import render_template
from flask import request
import os
import json
from os import listdir
app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_files():
	error = None
	dir = request.args.get('path','')
	dir = "/" + dir
	if dir == "":
		dir = "/"
	#print "DIR is %s" % dir
	#print os.listdir(dir)
	if os.path.isdir(dir): 
		mydirs = next(os.walk(dir))[1]
		myfiles = next(os.walk(dir))[2]
		#myfiles = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) ]
		print mydirs, myfiles
		if mydirs == "":
			return "No directories !"
		else:
			message = jsonify(Directories=mydirs, Files=myfiles)
			print message

			return render_template('index.html', message = message)
			#return jsonify(Directories=mydirs, Files=myfiles) 
	else:
		return "%s Dir doesn't exist" % dir
