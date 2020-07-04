import flask
from flask import request, jsonify
import numpy as np
from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import keras


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
	q = int (request.args['r1'])
	w = int(request.args['g1'])
	e = int(request.args['b1'])
	r = int(request.args['r2'])
	t = int(request.args['g2'])
	u= int(request.args['b2'])
	i = int(request.args['r3'])
	o = int(request.args['g3'])
	p = int(request.args['b3'])
	s = int(request.args['r4'])
	d = int(request.args['g4'])
	f = int(request.args['b4'])
	
	model = keras.models.load_model('aadya2.h5')
	te= np.array([q,w,e,r,t,u,i,o,p,s,d,f])
	g=(model.predict(np.reshape(te, (1,12)),batch_size=1))
	
	for x in g :
		a=x
		for y in a:
			z= y
	return str(y)
			
app.run(host = '0.0.0.0' , debug = True) 