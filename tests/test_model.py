import pytest
from poiapiexample import model  # passe das ggf. an deinen Modulnamen an

def test_calculate_addition():
    # Arrange
    params = {"a": 3.5, "b": 2.5}
    
    # Act
    result = model.calculate(params)
    
    # Assert
    assert result == {"result": 6.0}
