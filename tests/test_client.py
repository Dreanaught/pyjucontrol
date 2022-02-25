import unittest
import json
import hashlib
#from pyjucontrol.client import Client
from pyjucontrol import Client

class TestClient(unittest.IsolatedAsyncioTestCase):
    # setUp Client, login
    async def asyncSetUp(self):
        self.client = Client("#uname", "#pwd") # after checkout of your workspace replace with correct username & passwort
        _successful = await self.client.login()
        if not _successful:
            self.skipTest("external resource not available")
    
    # test get device data endpoint
    @unittest.skip("for now")
    async def test_endpoint_get_device_data(self):
        _data = await self.client._get_device_data()
        self.assertIsNotNone(_data)

    # test showlocation endpoint
    @unittest.skip("location is currently not of interest")
    async def test_endpoint_showlocation(self):
        _data = await self.client._showlocation()
        self.assertIsNotNone(_data)
        
    # test show endpoint
    @unittest.skip("for now")
    async def test_endpoint_show(self):
        _data = await self.client._show()
        self.assertIsNotNone(_data)

    async def test_update(self):
        _data = await self.client.update()
        self.assertIsNotNone(self.client.total_water_consumed)
        self.assertIsNotNone(_data)