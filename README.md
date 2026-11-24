# fhs_pipeline_26
My Fachhochschule Salzburg WS26 Pipeline Class repository.

This repo will contain VFX Tools & Python Scripts.

## Houdini Installation Instruction
Copy the file **houdini/fhs_pipeline.json** into the folder:
`Documents/Houdini<version>/packages`
and adjust in the file the line:
```json
  "FHS_PIPELINE": "D:/Documents/Development/FH_Salzburg/pipeline"
```
to the location where this folder is. 

## Dev
Powershell create and source devenv
```powershell
python -m venv .\venv
.\venv\Scripts\Activate.ps1
```
If you get a policy error in PowerShell, run:
```powershell 
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Required Packages: 
PySide6 & usd-core

Install PySide6 (or PySide2 for older dccs e.g. houdini 20.5)
```
pip install PySide6
```

Install Usd Core Python libraries 
```
pip install usd-core
```

When running the standalone python you might have to append the python directory to the python path to being able to import the fhs module. 

In the powershell the following command can be used for it.
```
$env:PYTHONPATH += ";d:\Documents\Development\FH_Salzburg\pipeline\python"
```