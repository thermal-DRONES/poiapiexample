# poiapiexample
an example submodule library for the thermal DRONES fastapi based POI-API Services 


## Requirements

- fastapi


please put your requirements in requrements.txt so that it can be installed with
```
pip install -r requirements.txt  
```

## Install

```
pip install poiapiexample
```

For development and testing (recommended):

```
git clone https://github.com/thermal-DRONES/poiapiexample.git
cd poiapiexample
pip install -e ".[dev]"
```

This installs the library in editable mode along with development tools like `pytest`.

## Run
Each module has its own usage example in the __name__=="__main__" section. You can run each module this way:

You can start your local uvicorn Webserver with fastapi, to test your code with. 
```
python -m poiapiexample.api
```

Now you can use your browser and type:
```
localhost:8000/docs/
```

here you get a comfortable user interface for your api.

With this structure we can integrate your library easily into the POIAPI Microservice container.



## 🧪 Tests

This project uses [`pytest`](https://docs.pytest.org/en/stable/) for unit testing. Tests are located in the `tests/` folder and primarily cover the core logic of the internal library — for example, the `calculate` function.

### 🔍 Example: `calculate`

The `calculate` function adds two input values and returns the result as a dictionary. The corresponding test ensures the calculation is correct:

```python
def test_calculate_addition():
    params = {"a": 3.5, "b": 2.5}
    result = model.calculate(params)
    assert result == {"result": 6.0}
```

### 🏁 Running the Tests

You can run the tests with:

```bash
pytest
```

To run a specific test file:

```bash
pytest tests/test_model.py
```

### 📦 Installing Test Dependencies

If `pytest` is not already installed, you can add it via pip:

```bash
pip install pytest
```
