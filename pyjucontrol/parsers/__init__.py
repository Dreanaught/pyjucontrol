"""pyjucontrol json parsers"""

class Parser:
    """Parser for all json messages"""

    def parse_get_device_data(self, json):
        """parse the get device data message"""
        if json["status"].upper() != "OK":
            return None
        data = json["data"]
        for listitem in data:
            self.parse_device_data(listitem)
        print("status:"+json["status"])

    def parse_device_data(self, json):
        """parse the device data"""
        for item in json.items():
            key = item[0]
            value = item[1]
            if(type(value) is str):
                print(key+":"+value)
            else:
                print(key+":"+type(value).__name__)
            
