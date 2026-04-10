from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Lambda, Conv2D, Dropout, Dense, Flatten
from src.config import INPUT_SHAPE

def build_model():
    model = Sequential([
        #normalize input into range from 1 to -1  (steps: divide every RGB val by 127.5, then -1) 
        Lambda(lambda x: x/127.5-1.0, input_shape=INPUT_SHAPE), #every input img is 66 pixels height x 200 width. 3 channels 

        #convolutional feature maps 
        #first num= num of filters, (5,5) = kernel size
        Conv2D(24, (5,5), activation='relu', strides=(2, 2)), #strides=(2, 2) = means move 2 pixels at a time, so skip every other pixel. reduces the size of the feature map (aka: img after convolution)
        Conv2D(36, (5,5), activation='relu', strides=(2, 2)),
        Conv2D(48, (5,5), activation='relu', strides=(2, 2)),
        Conv2D(64, (3,3), activation='relu', strides=(1, 1)),
        Conv2D(64, (3,3), activation='relu', strides=(1, 1)),

        Dropout(0.5), #better results with dropout. dropout randomly turns off half of the neurons during training to PREVENT OVERFITTING (MODEL MEMORIXING TRAINING DATA)
        Flatten(), #converts data into 1 value (vector). is needed for dense layers 
        Dense(100, activation='relu'),  #activation func adds non linearity 
        Dense(50, activation='relu'),
        Dense(10, activation='relu'),
        Dense(1),# is the output (steering angle)
    ])
    
    model.summary() #prints table with data about the model  

    return model
