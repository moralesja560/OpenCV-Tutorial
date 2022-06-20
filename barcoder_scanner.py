# Importing library
import cv2
from pyzbar.pyzbar import decode
import time

#arregla el autofocus de la camara

# Make one method to decode the barcode
def BarcodeReader(image):

	# read the image in numpy array using cv2
	img = image
      
    # Decode the barcode image
	detectedBarcodes = decode(img)
      
    # If not detected then print the message
	if detectedBarcodes:
          # Traverse through all the detected barcodes in image
		for barcode in detectedBarcodes: 
		# Locate the barcode position in image
			(x, y, w, h) = barcode.rect
			
			# Put the rectangle in image using
			# cv2 to heighlight the barcode
			cv2.rectangle(img, (x-10, y-10),
			(x + w+10, y + h+10),
			(255, 0, 0), 2)
			
			
			if barcode.data!="":
			# Print the barcode data
				print(barcode.data)
				time.sleep(3)
				#print(barcode.type)
	#else:
		#print("Barcode Not Detected or your barcode is blank/corrupted!")
	#Display the image
	cv2.imshow("Image", img)
	

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(1,cv2.CAP_DSHOW)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)




while True:
	_, frame = cap.read()
	BarcodeReader(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
