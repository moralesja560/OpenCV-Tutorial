from random import randint
import cv2
import os
import numpy as np
import time
from dotenv import load_dotenv
from urllib.parse import quote
from urllib.request import Request, urlopen
import json
controlvar = 0
load_dotenv()
JorgeMorales = os.getenv('JorgeMorales')
Grupo_WT = os.getenv('WATERTANK')
AngelI = os.getenv('AngelI')
token_bot = os.getenv('api_token')

RTSP_URL = 'rtsp://user:user@10.65.96.76:8554/streaming/channels/1001'
os.environ['OPENCV_FFMPEG_CAPTURE_OPTIONS'] = 'rtsp_transport;udp'
cap = cv2.VideoCapture(RTSP_URL, cv2.CAP_FFMPEG)
#cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

#first min values then max values
myColors = ([[0,8,241,179,94,255]])
#please make the first numbers of each color different.
#hue min , sat min, value min  hue max, sat max, value max.

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
		if area>250:
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
	if exit_var == None:
		controlvar +=1
		print(f"alarm detected  {controlvar}")
		if(controlvar % 1000 == 0):
			print(controlvar)
			send_message(JorgeMorales,quote(f"URGENTE: Revisar tanques de Heat Line"),token_bot)
			controlvar = 1
		return
		


while True:
	success, img = cap.read()
	img_Result = img.copy()
	findColor(img,myColors)
	cv2.imshow('Contours', img_Result)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
