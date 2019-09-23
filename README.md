# BMI160

```python
from machine import Pin, I2C
from BMI160 import BMI160_I2C
i2c = I2C(sda=Pin(32), scl=Pin(33))
bmi160 = BMI160_I2C(i2c)
```