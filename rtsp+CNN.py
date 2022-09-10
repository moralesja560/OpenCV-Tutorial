from fileinput import filename
import cv2
import os
import tensorflow as tf
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)

def load_and_prep_image(filename,img_shape=224):
	"""
	Reads an image from filename, turns it into a tensor and reshapes it to the selected shape (eg 224)
	"""
	#read in the image (modified because opencv)
	#img = tf.io.read_file(filename)
	img = filename
	#decode the image into a tensor
	img = tf.image.decode_image(img)
	#resize the image
	img = tf.image.resize(img, size=[img_shape,img_shape])
	#rescale the image
	img = img/255
	return img


#keras model load
new_model = tf.keras.models.load_model(r'C:\Users\moralesja.group\Documents\SC_Repo\NeuralNetwork\CNN\dogcatmodel')
font = cv2.FONT_HERSHEY_SIMPLEX
  
while True:
	# Capture the video frame
	# by frame
	ret, img = vid.read()
	image = cv2.resize(img,dsize=(224,224), interpolation = cv2.INTER_CUBIC) 
	final_data = new_model.predict(np.expand_dims(image, axis=0))
	if final_data <0.30:
		print(f"It's a cat {final_data}")
		cv2.putText(img, 'CAT', (10,450), font, 3, (0, 255, 0), 2, cv2.LINE_AA)
	elif final_data > 0.70 and final_data < 1:
		print(f"It's a dog {final_data}")
		cv2.putText(img, 'DOG', (10,450), font, 3, (255, 0, 0), 2, cv2.LINE_AA)
	cv2.imshow("Data",img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
  
# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()