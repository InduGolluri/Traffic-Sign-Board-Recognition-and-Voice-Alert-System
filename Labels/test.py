def upload():
	if request.method == 'POST':
        # Get the file from post request
		f = request.files['file']
		file_path = secure_filename(f.filename)
		f.save(file_path)
        # Make prediction
		result = image_processing(file_path)
		s = [str(i) for i in result]
		a = int("".join(s))
		result = "Predicted Traffic Sign is: " +classes[a]
		os.remove(file_path)
		engineio = pyttsx3.init()
		engineio.say(result)
		results=engineio.runAndWait()
		return result
		return results        
	return None
