import cv2
import os
import numpy as np
import time
from dotenv import load_dotenv
from urllib.parse import quote
from urllib.request import Request, urlopen
import json
import pytesseract
import requests
from random import randint, random
import sys

controlvar = 0
load_dotenv()
JorgeMorales = os.getenv('JorgeMorales')
Grupo_WT = os.getenv('WATERTANK')
AngelI = os.getenv('AngelI')
token_bot = os.getenv('api_token')

RTSP_URL = 'rtsp://root:MubMex30..@10.65.68.29/axis-media/media.amp'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#first min values then max values
myColors = ([[31,65,0,34,255,255]])
#please make the first numbers of each color different.
#hue min , sat min, value min  hue max, sat max, value max.

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

def send_message(user_id, text,token):
	global json_respuesta
	url = f"https://api.telegram.org/{token}/sendMessage?chat_id={user_id}&text={text}"
	#resp = requests.get(url)
	#hacemos la petición
	try:
		respuesta  = urlopen(Request(url))
	except Exception as e:
		print(f"Ha ocurrido un error al enviar el mensaje: {e}")
	else:
		#recibimos la información
		cuerpo_respuesta = respuesta.read()
		# Procesamos la respuesta json
		json_respuesta = json.loads(cuerpo_respuesta.decode("utf-8"))
		print("mensaje enviado exitosamente")

####-----------------------------------End of Telegram message Services------#


def getContours(img):
	contours,hierarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
	x,y,w,h = 0,0,0,0
	for cnt in contours:
		area = cv2.contourArea(cnt)
		#print(area)
		if area>2000:
			cv2.drawContours(img_Result, cnt, -1, (255, 0, 0), 3)
			peri = cv2.arcLength(cnt,True)
			approx = cv2.approxPolyDP(cnt,0.02*peri,True)
			x, y, w, h = cv2.boundingRect(approx)
			return None
	return x+w//2,y

def findColor(img,myColors):
	global controlvar
	for color in myColors:
		lower = np.array(color[0:3])
		upper = np.array(color[3:6])
		imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
		mask = cv2.inRange(imgHSV,lower,upper)
		exit_var = getContours(mask)
	if exit_var is not None:
		controlvar +=1
		print(f"alarm detected  {controlvar}")
		if(controlvar % 1000 == 0):
			print(controlvar)
			#send_message(JorgeMorales,quote(f"URGENTE: Revisar tanques de Heat Line"),token_bot)
			controlvar = 1
		return

def read_from_img(img):
	processed_text = "cadena vacia"
	#wait for branch merging then try to adjust screenshot area to allow tesseract to read accurately
	#check if program is installed
	file_exists2 = os.path.exists('C:/Program Files/Tesseract/tesseract.exe')
	if file_exists2 == False:
		#there's not Tesseract Installed
		print("No encontré Tesseract")
		return
	# read image
	image = img
	# configurations
	config = ('-l eng --oem 3 --psm 7')
	# pytessercat
	pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract/tesseract.exe'
	text = pytesseract.image_to_string(image, config=config)
	# print text
	text = text.split('\n')
	for letter in text:
	#check for nonexistant HU
		if len(letter)<3:
			continue
		else:
			processed_text = f"El error tenía esto {letter}, pero no pude detectar caracteres"

	return processed_text

def send_photo(user_id, image,token):
	img = open(image, 'rb')
	#img = image
	TOKEN = token
	CHAT_ID = user_id
	url = f'https://api.telegram.org/{TOKEN}/sendPhoto?chat_id={CHAT_ID}'
	print(url)
	#resp = requests.get(url)
	#hacemos la petición

	respuesta = requests.post(url, files={'photo': img})

	if '200' in str(respuesta):
		print(f"mensaje enviado exitosamente con código {respuesta}")
	else:
		print(f"Ha ocurrido un error al enviar el mensaje: {respuesta}")


control_number = 0
while True:
	success, frame1 = cap.read()
	img = frame1[370:600,600:900]
	img2 = frame1[490:630,190:370]
	img3 = frame1[150:900,0:900]

	control_number += 1
	print(control_number)
	if(control_number % 5 == 0):
		rutafoto = resource_path(f"resources\img{randint(1,90000)}.jpg")
		print(rutafoto)
		cv2.imwrite(rutafoto, img3)
		send_photo(Grupo_WT,rutafoto,token_bot)
		continue 
	time.sleep(300)
	#img_Result = img.copy()
	#findColor(img,myColors)
	#cv2.imshow('Contours', img_Result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
