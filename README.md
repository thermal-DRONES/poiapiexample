# fastapiexample
an example submodule library for the thermal DRONES fastapiServices (POI-Api)


## Requirements

- fastapi


please put your requirements in requrements.txt so that it can be installed with
```
pip install -r requirements.txt  
```

## Install

```
pip install fastapiexample
```

For development and testing (recommended):

```
git clone https://github.com/thermal-DRONES/fastapiexample.git
cd fastapiexample
pip install -e ".[dev]"
```

This installs the library in editable mode along with development tools like `pytest`.

## Run
Each module has its own usage example in the "name"==__main__ section. You can run each module this way:
 
```
python -m fastapiexample.submodule
```

## api 