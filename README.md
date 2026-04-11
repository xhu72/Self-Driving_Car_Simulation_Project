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

