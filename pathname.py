from flask import Flask
from flask import jsonify
from flask import request
import os
import json
from os import listdir
app = Flask(__name__)

@app.route('/', methods=['GET'])
def display_files():
	error = None
	dir = request.args.get('dirs','')
	dir = "/" + dir
	#print "DIR is %s" % dir
	if dir == "":
		dir = "/"
	#print "DIR is %s" % dir
	#print os.listdir(dir)
	if os.path.isdir(dir): 
		mylist = os.listdir(dir)
		print mylist
		if mylist == "":
			return "No files !"
		else:
			return jsonify(Directories=mylist) 
	else:
		return "%s Dir doesn't exist" % dir
