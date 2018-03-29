#!/usr/bin/env python3
import os
import unittest
import time
from unittest import mock
from flask import json

import plantserver

import test_values


class PlantServerTestCase(unittest.TestCase):

    def setUp(self):
        plantserver.app.config['TESTING'] = True
        
        self.app = plantserver.app.test_client()

    def test_home(self):
        rv = self.app.get('/', follow_redirects=True)
        assert 'PlantServer' in rv.data.decode('utf-8')
    
    def test_log(self):
         mock_sensorjson = json.dumps({
             'version': '0.1',
             'data': {
                 'moisture': 1,
                 'light': 0.123
             }
         })
         rv = self.app.post('/log', follow_redirects=True, data=mock_sensorjson)

if __name__ == '__main__':
    unittest.main()
