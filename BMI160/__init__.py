from  BMI160 import registers
from  BMI160 import commands
from  BMI160 import definitions
from time import sleep_ms

class BMI160:
    def __init__(self):
        # Issue a soft-reset to bring the device into a clean state
        self._reg_write(registers.CMD, commands.SOFT_RESET)
        sleep_ms(1)

        # Issue a dummy-read to force the device into I2C comms mode
        self._reg_read(0x7F)
        sleep_ms(1)

        # Power up the accelerometer
        self._reg_write(registers.CMD, commands.ACC_MODE_NORMAL)
        # Wait for power-up to complete
        while (1 != self._reg_read_bits(registers.PMU_STATUS, definitions.ACC_PMU_STATUS_BIT, definitions.ACC_PMU_STATUS_LEN)):
            pass
        sleep_ms(1)

        # Power up the gyroscope
        self._reg_write(registers.CMD, commands.GYR_MODE_NORMAL)
        sleep_ms(1)
        # Wait for power-up to complete
        while (1 != self._reg_read_bits(registers.PMU_STATUS, definitions.GYR_PMU_STATUS_BIT, definitions.GYR_PMU_STATUS_LEN)):
            pass
        sleep_ms(1)

        self.set_full_scale_gyro_range(definitions.GYRO_RANGE_250, 250.0)
        self.set_full_scale_accel_range(definitions.ACCEL_RANGE_2G, 2.0)

        # Only PIN1 interrupts currently supported - map all interrupts to PIN1
        self._reg_write(registers.INT_MAP_0, 0xFF)
        self._reg_write(registers.INT_MAP_1, 0xF0)
        self._reg_write(registers.INT_MAP_2, 0x00)

    def _reg_read_bits(self, reg, pos, len):
        b = self._reg_read(reg)
        mask = (1 << len) - 1
        b >>= pos
        b &= mask
        return b

    def _reg_write_bits(self, reg, data, pos, len):
        b = self._reg_read(reg)
        mask = ((1 << len) - 1) << pos
        data <<= pos  # shift data into correct position
        data &= mask  # zero all non-important bits in data
        b &= ~(mask)  # zero all important bits in existing byte
        b |= data     # combine data with existing byte
        self._reg_write(reg, b)

    ## Set full-scale gyroscope range.
    # param range New full-scale gyroscope range value
    # see getFullScaleGyroRange()
    def set_full_scale_gyro_range(self, range, real):
        self._reg_write_bits(registers.GYRO_RANGE, range, definitions.GYRO_RANGE_SEL_BIT, definitions.GYRO_RANGE_SEL_LEN)

    ## Set full-scale accelerometer range.
    # param range New full-scale accelerometer range setting
    # see getFullScaleAccelRange()
    # see BMI160AccelRange 
    def set_full_scale_accel_range(self, range, real):
        self._reg_write_bits(registers.ACCEL_RANGE, range, definitions.ACCEL_RANGE_SEL_BIT, definitions.ACCEL_RANGE_SEL_LEN)




class BMI160_I2C(BMI160):
    def __init__(self, i2c, addr=0x69):
        self.i2c = i2c
        self.addr = addr
        super().__init__()

    def _reg_write(self, reg, data):
        self.i2c.writeto(self.addr, bytes([reg, data]))

    def _reg_read(self, reg):
        self.i2c.writeto(self.addr, bytes([reg]))
        # read one byte
        return self.i2c.readfrom(self.addr, 1)[0]