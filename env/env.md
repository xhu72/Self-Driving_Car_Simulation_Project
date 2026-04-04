# Self-Driving_Car_Simulation_Project

# Setting Up Your Conda Environment

You can set up your environment by running the following commands in your terminal.

## 1. Create the environment
```powershell
conda create --name final_project --file "package_list (2).txt"
```
## 2. Activate the Conda Environment

To activate your environment, run the following command in PowerShell:

```powershell
conda activate final_project
```

However, it fails because the file "package_list(2).txt"  contains strict "build hashes" (e.g., =h62dcd97_1010).

To bypass this issue, we can extract just the package names and versions into a standard pip requirements.txt file.



# Self-Driving Car Simulation Project Setup from `requirements.txt`

## 1. Create Project Folder
```bash
mkdir computer_vision
cd computer_vision
```


## 2. Check Python Installation
```bash
python --version
```
(if not installed, install it version 3.11.1)

## 3. Create Virtual Environment
in cmd
```bash
C:\Users\larry\AppData\Local\Programs\Python\Python311\python.exe -m venv venv311 
```
or

```bash
python -m venv venv
```

## 4. Activate Virtual Environment (PowerShell)
```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\activate
```

## 5. Clone Repository
```bash
cd venv
git clone https://github.com/xhu72/Self-Driving_Car_Simulation_Project.git
cd .\Self-Driving_Car_Simulation_Project\
```

## 6. Check Conda Installation
```bash
where conda 
```
(If not installed, install Miniconda or Anaconda)

## 7. Create Conda Environment
```bash
conda create --name final_project python=3.11 -y
conda activate final_project
```

## 8. Upgrade pip
```bash
python -m pip install --upgrade pip setuptools wheel
python -m pip install --upgrade pip
```

## 9. Install Critical Packages (via conda)
```bash
conda install h5py yarl greenlet
```

## 10. Install Remaining Dependencies
```bash
python -m pip install -r env/requirements.txt
```