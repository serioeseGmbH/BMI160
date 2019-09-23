## bit field offsets and lengths
ACC_PMU_STATUS_BIT  = const(4)
ACC_PMU_STATUS_LEN  = const(2)
GYR_PMU_STATUS_BIT  = const(2)
GYR_PMU_STATUS_LEN  = const(2)
GYRO_RANGE_SEL_BIT  = const(0)
GYRO_RANGE_SEL_LEN  = const(3)
GYRO_RATE_SEL_BIT   = const(0)
GYRO_RATE_SEL_LEN   = const(4)
GYRO_DLPF_SEL_BIT   = const(4)
GYRO_DLPF_SEL_LEN   = const(2)
ACCEL_DLPF_SEL_BIT  = const(4)
ACCEL_DLPF_SEL_LEN  = const(3)
ACCEL_RANGE_SEL_BIT = const(0)
ACCEL_RANGE_SEL_LEN = const(4)

## Gyroscope Sensitivity Range options
# see setFullScaleGyroRange()
GYRO_RANGE_2000     = const(0)    # +/- 2000 degrees/second
GYRO_RANGE_1000     = const(1)    # +/- 1000 degrees/second
GYRO_RANGE_500      = const(2)    # +/-  500 degrees/second
GYRO_RANGE_250      = const(3)    # +/-  250 degrees/second
GYRO_RANGE_125      = const(4)    # +/-  125 degrees/second

## Accelerometer Sensitivity Range options
# see setFullScaleAccelRange()
ACCEL_RANGE_2G      = const(0X03) # +/-  2g range
ACCEL_RANGE_4G      = const(0X05) # +/-  4g range
ACCEL_RANGE_8G      = const(0X08) # +/-  8g range
ACCEL_RANGE_16G     = const(0X0C) # +/- 16g range

FOC_ACC_Z_BIT       = const(0)
FOC_ACC_Z_LEN       = const(2)
FOC_ACC_Y_BIT       = const(2)
FOC_ACC_Y_LEN       = const(2)
FOC_ACC_X_BIT       = const(4)
FOC_ACC_X_LEN       = const(2)
FOC_GYR_EN          = const(6)