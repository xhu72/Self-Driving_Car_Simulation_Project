import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
import socketio
import eventlet
import eventlet.wsgi
import numpy as np
from flask import Flask
import base64
from io import BytesIO
from PIL import Image
from src.image_utils import preprocess #import preprocessing func from src/image_utils file 
from src.model import build_model

sio = socketio.Server()
app = Flask(__name__)
model = None

MAX_SPEED = 30
MIN_SPEED = 15
speed_limit = MAX_SPEED

@sio.on('telemetry')
def telemetry(sid, data):
    if data:
        steering_angle = float(data['steering_angle'])
        throttle = float(data['throttle'])
        speed = float(data['speed'])
        print(f"Steering Angle: {steering_angle}  |  Throttle: {throttle}  |  Speed: {speed}")
        
        image = Image.open(BytesIO(base64.b64decode(data['image'])))

        try:
            image = np.asarray(image)
            image = preprocess(image)
            image = np.array([image])

            steering_angle = float(model.predict(image, batch_size=1))
            
            global speed_limit # is needed so that speed_limit var outside of this func gets modified 

            #if streering is straight then go fast, otherwise (on turn), go slow. calculates the scaled speed. speed can be between 15 to 30 range. 
            #(MAX_SPEED - MIN_SPEED) is the range of the speed (15).  (1.0 - abs(steering_angle) = assigns a val of 1 if straight turn and 0 for sharp turn
            speed_limit = MIN_SPEED + (MAX_SPEED - MIN_SPEED) * (1.0 - abs(steering_angle))#abs = absolute val 

            #Penalize 
            throttle = 1.0 - abs(steering_angle)**2 - (speed/speed_limit)**2
            throttle = max(0.0, min(1.0, throttle)) #

            sendControl(steering_angle, throttle)
        except Exception as e:
            print(e) 
    else: #runs if no telemetry data is received, so that doesnt crash when I stop getting data 
        sio.emit('manual', data={}, skip_sid=True) #switch driving sim to manual driving mode 

@sio.on('connect')
def connect(sid, environ): #sid = session id of the car simulator when connected 
    print('\n***CONNECTED TO SIMULATOR***\n', sid)
    sendControl(0, 0)

def sendControl(steering, throttle):
    sio.emit('steer', data={
        'steering_angle' : steering.__str__(),
        'throttle' : throttle.__str__()
    })

if __name__ == "__main__":
    model = build_model() #recreate the CNN structure before loading the weights. makes sure your architecture is the same as it was in train.py
    #important!!, must change this to the last created model (model with biggest number in the title after running train.py) 
    model.load_weights('model-012.h5') #load the trained params into the neural network structure 
    
    app = socketio.Middleware(sio, app)
    eventlet.wsgi.server(eventlet.listen(('', 4567)), app)