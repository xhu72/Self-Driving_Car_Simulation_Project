
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