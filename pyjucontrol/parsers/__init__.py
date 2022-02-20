"""pyjucontrol json parsers"""

class Parser:
    """Parser for all json messages"""

    def parse_get_device_data(self, json):
        """parse the get device data message"""
        for firstlevel in json:
            print(firstlevel)