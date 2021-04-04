import json
#Not the bet way but immutable values can be set here.
class Config(object):
    def __init__(self):
        self.dict = {
            'frequency' : 30,
            'front_led_address': [hex(0x70), hex(0x76)], # check i2cdetect -r -y 8 before intializing addresses
            'back_led_address' : [hex(0x72), hex(0x73)],
            'front_led_frequency': 30,
            'back_led_frquency' : 30,
            'main_led_frequency' : 30,
            'main_led_pin': 18,
            'lidar_port': '/dev/ttyUSB0'
        }

        #No plans yet
        self.folders = {

        }

    def get_configfile(self) -> dict:
        return self.dict
    
    def current_config_file(self):
        print(self.dict)

