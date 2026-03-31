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

# Setting Up Your Conda Environment from `requirements.txt`

Since we already generated the `requirements.txt` file, you can follow these steps:

## 1. Create the new environment

```powershell
conda create --name final_project python=3.8.12 -y
```
## 2. Activate the environment

```powershell
conda activate final_project
```

## 3. Install the dependencies

```powershell
pip install -r requirements.txt