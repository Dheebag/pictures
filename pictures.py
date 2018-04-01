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
        my_base_url = request.base_url
        print "My base url %s" % my_base_url
	my_path= os.path.join(request.args.get('path',''))
	my_list_of_dict=[]

	if dir == "":
		dir = "/"
	if os.path.isdir(dir):
		mydirs = next(os.walk(dir))[1]
		for d in mydirs:
			my_list_of_dict.append({"Directory":d}) 
		
		myfiles = next(os.walk(dir))[2]
		for f in myfiles:
			my_list_of_dict.append({"File":f}) 
		#myfiles = [ f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir,f)) ]
		print my_list_of_dict
		for i in my_list_of_dict:
			if i.get('Directory') != None:  
				print i.get('Directory') 
			else:
				print i.get('File')
		
		if my_list_of_dict == "":
			return "No directories !"
		else:

			return render_template('index.html', dir=os.listdir(dir),my_base_url=my_base_url,my_path=my_path,my_dict = my_list_of_dict, files=myfiles)
			#return jsonify(Directories=mydirs, Files=myfiles) 
	else:
		return "%s Dir doesn't exist" % dir
