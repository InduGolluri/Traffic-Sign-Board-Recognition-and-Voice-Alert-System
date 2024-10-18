def image_processing(img):
	model = load_model('./model/traffic.h5')
	data=[]
	image = Image.open(img)
	image = image.resize((30,30))
	data.append(np.array(image))
	X_test=np.array(data)
	Y_pred = model.predict_classes(X_test)
	return Y_pred
