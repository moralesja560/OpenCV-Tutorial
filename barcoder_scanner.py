# Importing library
from sqlite3 import enable_callback_tracebacks
import cv2
from pyzbar.pyzbar import decode
import time

#arregla el autofocus de la camara
barcodes_f = []

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
			
			
			if barcode.data!="" and len(barcodes_f)>0:
			# Print the barcode data
				#print(barcode.data)
				#if not found, please store it
				if barcode.data in barcodes_f[-1]:
					#print(f"already stored data {barcode.data}")
					pass
				else:
					barcodes_f.append(barcode.data)
					print(f"data stored {barcode.data}")
				#time.sleep(3)
				#print(barcode.type)
			elif barcode.data!="" and len(barcodes_f)==0:
				if barcode.data in barcodes_f:
					#print(f"already stored data {barcode.data}")
					pass
				else:
					barcodes_f.append(barcode.data)
					print(f"data stored {barcode.data}")

	#Display the image
	cv2.imshow("Image", img)
	

frameWidth = 800
frameHeight = 600

cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.set(3,frameWidth)
cap.set(4,frameHeight)
cap.set(10,150)



while True:
	_, frame = cap.read()
	BarcodeReader(frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		print(f"Estos fueron los códigos encontrados {barcodes_f}")
		break
