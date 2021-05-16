from flask import render_template, request,jsonify
from flask import redirect, url_for
import os , io , sys
from PIL import Image
from app.utils import trainning_history
from flask import json
import base64
from .yolodetect import runModel
import numpy as np
import cv2

#UPLOAD_FLODER = 'static/uploads'

def index():
    return render_template('index.html')

def fruits360():

	iv3 = trainning_history('./static/history/Model.InceptionV3.History.txt')
	res = trainning_history('./static/history/Model.ResNet101.History.txt')
	xcep = trainning_history('./static/history/Model.Xception.History.txt')
	vgg = trainning_history('./static/history/Model.VGG16.History.txt')
	matrix = trainning_history('./static/history/matrix.txt').tolist()
	#report = trainning_history('./static/history/f1report.txt')
	preprocess = trainning_history('./static/history/preprocess.txt')
	pcessk = [k for (k, v) in (preprocess.items())]
	pcesskxais = list(range(1, len(pcessk)+1))
	pcessv = [int(v) for (k, v) in (preprocess.items())]
	classes = trainning_history('./static/history/classes.txt')
	epochs = list(range(1, len(iv3['accuracy'])+1))
	return render_template('fruits360.html', 
		iv3=iv3, 
		res=res, 
		xcep = xcep,
		vgg = vgg,
		matrix = matrix,
		classes = json.dumps(classes),
		pcessk = pcessk,
		pcesskxais = pcesskxais,
		pcessv = pcessv,
		epochs=epochs)

def fruitsyolov3():
	return render_template('yolo.html')

def testyolov3():
	return render_template('test.html')

def mask_image():
	print(request.files , file=sys.stderr)
	file = request.files['image'].read() ## byte file
	npimg = np.fromstring(file, np.uint8)
	img = cv2.imdecode(npimg,cv2.IMREAD_COLOR)
	img,labelnames = runModel(img)

	img = Image.fromarray(img.astype("uint8"))
	rawBytes = io.BytesIO()
	img.save(rawBytes, "JPEG")
	rawBytes.seek(0)
	img_base64 = base64.b64encode(rawBytes.read())
	return jsonify({'status':str(img_base64), 'labelnames': labelnames})

def test():
	print("log: got at test" , file=sys.stderr)
	return jsonify({'status':'succces'})
