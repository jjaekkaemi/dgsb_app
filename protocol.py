REQ_START_MEASURE = bytearray([0x02, 0x30, 0x36, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
# REQ_START_MEASURE = bytearray([0x02, 0x01, 0x01, 0x01, 0x03])
REQ_STOP_MEASURE = bytearray([0x02, 0x30, 0x32, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_SPO2 = bytearray([0x02, 0x30, 0x33, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_HR = bytearray([0x02, 0x30, 0x39, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_WALK = bytearray([0x02, 0x30, 0x35, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_RUN = bytearray([0x02, 0x30, 0x36, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_ALL = bytearray([0x02, 0x30, 0x37, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_BATT =bytearray([0x02, 0x30, 0x38, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_SCD = bytearray([0x02, 0x30, 0x39, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_ACC = bytearray([0x02, 0x31, 0x30, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_GYRO = bytearray([0x02, 0x31, 0x31, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_GET_MAX32630 = bytearray([0x02, 0x31, 0x32, 0x5E, 0x30, 0x31, 0x5E, 0x01, 0x03])
REQ_SET_MAX32630_CMD = '13'