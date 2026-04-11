__ENVIRONMENT SETUP__

To create an exact conda environment from `environment.yml` :

```bash

conda env create -f environment.yml

```
If this command does not work due to Conda not being recognized. Install anaconda3 if you do not have it installed. 
  If you already have Anaconda installed or you just finished installing Anaconda, open the "Anaconda Powershell Prompt" and type:
   ```bash
   conda --version 
   ```
   to check that you have Anaconda and it is working. Then, if the previous command ran successfully, in Anaconda Prompt, run:

   ```bash
   conda init powershell
   ```
   Close and reopen this VScode project.
   To check that everything works, type this in this VScode project: 
   ```bash
   conda --version
   ```
Now, you should be able to run:
```bash

conda env create -f environment.yml

```

 

SKIP TO HERE IF THE "conda env create -f environment.yml" COMMAND WORKED!
LAST STEP:

Now to activate the env, run:

``` bash

conda activate car-cnn

```
```

__APPROACH__
The solution is reliant on Behavioural Cloning to teach Convolutional Neural Network (CNN) to steer the  car autonomously in Udacity simulator.
**Data Collection and Processing:** 
The images are saved from three simulated front-facing cameras (center, left, and right) together with the steering angle telemetry in real-time. Left and right camera images are used to simulate recovery scenarios through application of a calculated offset to the recorded steering angle.
**CNN Architecture** 
An end-to-end regression architecture was employed where the model begins with a Lambda layer to normalize pixel values. Then, it is followed by 5 Convolutional layers (`Conv2D` with ReLU activations) to extract features such as spatial lane and road features. The data is then flattened and passed through a Dropout layer to prevent overfitting and scaled down using Dense fully-connected layers (100 -> 50 -> 10 -> 1) to predict a precise steering angle.
**Real-Time Control Loop** 
The physical simulation connection is created in `TestSimulation.py` using Python `socketio` and asynchronous event loops (`eventlet`). The simulator streams live frames and the web socket server pipes the images to the model's prediction pipeline and immediately predicting the steering angle and appropriate throttle directly back to the Unity simulator engine.

__MAJOR CHALLENGES AND HOW WE ADDRESSED THEM__

**Challenge - Overfitting to a specific track and lighting** 
The simulator tracks are static so the model had a high risk of memorizing the background scenery instead of actually learning how to identify the road lines.
**How it was addressed**
A real-time image augmentation pipeline was implemented (`src/augmentations.py`). A variation of the input images was created during training using a continuous batch generator before the network sees them. This includes applying random horizontal flips, injecting artificial shadows, skewing the overall image brightness and panning the images which multiplied the training dataset while forcing the model to care about high-contrast road features instead of the background environment.
**Challenge - Navigating sharp turns and preventing straight line bias** 
Standard driving mostly involves keeping the wheel straight which skews the dataset heavily towards a `0` steering angle resulting in model poorly predicting sharp corners and just preferring to drive straight.
**How it was addressed**
This was solved with enriching the data. The model was fed with simulated examples of how to steer hard back into the middle of the track by pulling from the offset left and right cameras. Dynamic horizontal translations were also introduced during augmentation to position the car at the edge of the road and thus training the network to navigate out of failure cases before crashing into a lake or a wall.




__TO RUN THE CODE__

Be in the project root folder

Run the following commands:


``` bash
python -m src.config
python -m src.augmentations
python -m src.data_generator
python -m src.dataset
python -m src.image_utils
python -m src.model

python train.py
python TestSimulation.py 
```

If TestSimulation.py does not run, that likely that means the specified model in TestSimulation.py does not exist (ex: model-012.h5), in that case, change the model name to the one with the biggest numeric value in the following line of code:  
``` bash
model.load_weights('model-012.h5')
```

__TO SEE HOW THE CODE RUNS IN THE UDACITY CAR SIMULATOR__

After running "python TestSimulation.py ", open your __beta_simulator.exe__, in the popup model, click "Play!". 
Once you see the main Udacity Car Driving Simulator screen, click on "autonomous mode".


You should now see the car driving automously! 

__UDACITY CAR SIMULATION DEMO__

See the demo of self-driving simulation using CNN [here](https://youtu.be/aMdI5PAKO64).