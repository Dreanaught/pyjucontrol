"""JU-Control API access."""
from typing import Any, Dict, List, Optional
from aiohttp import ClientSession
from yarl import URL
import hashlib

BASE_URL: URL = URL("https://www.myjudo.eu/").with_path("/interface")

class Client:
    """JU-Control client.
    """
    _token = None

    def __init__(
        self,
        username: str,
        password: str,
        session: Optional[ClientSession] = None,
    ):
        self._username = username
        self._passwordHashed = hashlib.md5(password.encode('UTF-8')).hexdigest()
        if session:
            self._session = session
            self._managed_session = False
        else:
            self._session = ClientSession()
            self._managed_session = True

    @property
    def token(self) -> str:
        """Return currently used token"""
        return self._token
    
    async def login(self) -> bool:
        """Login to api witn given username and password"""
        query = {
            "group": "register",
            "command": "login",
            "name": "login",
            "user": self._username,
            "password": self._passwordHashed,
            "role": "customer",
        }
        _login_url = BASE_URL.with_query(query)

        async with self._session.get(_login_url, raise_for_status=True) as resp:
            json = await resp.json()
            if not resp:
                return False
            elif json.get("status").upper() == "OK":
                self._token = json.get("token")
                return True 
            else :
                return False

    async def update(self) -> bool:
        """Reach out to online service to update data.
        
        This should be rate limited.
        """
        _deviceData = await self._get_device_data()
        #_locationData = await self._showlocation()
        #_showData = await self._show()

        #print(_deviceData)
        _device_map = await self._parse_get_device_data(_deviceData)

    async def _parse_get_device_data(self, json):
        _valid = json.get("status").upper() == "OK"
        _data = json.get("data")

        for device in _data:
            _serialnumber = device.get("serialnumber")
            _installation_data = device.get("installation_date")
            _online_status = device.get("status")
            _software_version = device.get("sv")
            _hardware_version = device.get("hv")
            _raw_data = device.get("data")
            for entry in _raw_data:
                _da = entry.get("da")
                _device_type = entry.get("dt")
                _device_sv = entry.get("sv")
                _device_hv = entry.get("hv")
                _device_data = entry.get("data")
                _valid_data = dict()
                for k, v in _device_data.items():
                    if k == "lu" :
                        pass
                    elif v is None:
                        pass
                    elif v.get("st").upper() == "OK":
                        _k_it = int(k)
                        _valid_data[_k_it] = v.get("data")
            print(_valid_data)

            # parsing data out of given bytestreams
            _8:str = _valid_data.get(8)
            if len(_8) == 8:
                total_water_consumed = self.split_by_two_reverse(_8) # in liter
            _9:str = _valid_data.get(9)
            if len(_9) == 8:
                total_soft_water_consumed = self.split_by_two_reverse(_9) # in liter
            _791 = _valid_data.get(791)
            if len(_791) == 66:
                _791 = _791.split(":")[1]
                regeneration_count = int(_791[62:64] + _791[60:62] ,base=16)
            _90 = _valid_data.get(90)
            if len(_90) == 4:
                hardness_water_raw = int(_90[2:4] + _90[0:2],base=16)
            _94 = _valid_data.get(94)

    def split_by_two_reverse(self, string)-> int:
        reversed = string[6:8] + string[4:6] + string[2:4] + string[0:2]
        return int(reversed, base=16)

    async def _get_device_data(self):
        """Call the get device data endpoint"""
        query = {
            "token": self._token,
            "group": "register",
            "command": "get device data",
        }
        _url = BASE_URL.with_query(query)
        async with self._session.get(_url, raise_for_status=True) as resp:
            return await resp.json()

    async def _showlocation(self):
        """Call the showlocation endpoint"""
        query = {
            "token": self._token,
            "group": "register",
            "command": "showlocation",
        }
        _url = BASE_URL.with_query(query)
        async with self._session.get(_url, raise_for_status=True) as resp:
            return await resp.json()
    
    async def _show(self):
        """Call the show endpoint"""
        query = {
            "token": self._token,
            "group": "register",
            "command": "show",
        }
        _url = BASE_URL.with_query(query)
        async with self._session.get(_url, raise_for_status=True) as resp:
            return await resp.json()


