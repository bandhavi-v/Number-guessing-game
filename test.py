import os
import server
import httplib2
import unittest
import requests

http = httplib2.Http()
class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_checking_server_response(self):
        
		#index_url --> URL for index page in the server
        index_url = 'http://localhost:5000/'
        response = http.request(index_url)

        #checking the response of GET request
        json_status = response[0]['status']
        self.assertEqual(json_status, '200')

        #checking if the server response from GET request is JSON
        json_content = response[0]['content-type']
        self.assertEqual(json_content, 'application/json')

    def test_checking_input_response(self):
        
		#game_url --> URL for posting the user input
        game_url = 'http://127.0.0.1:5000/guess'
        #int_input --> Input from the user (Integer)
        int_input = '{"value":3}'
        headers = {'content-type': 'application/json'}

        #checking... if input is Integer
        json_content = requests.post(game_url, data=int_input, headers=headers)
        int_response = str(json_content).translate(str.maketrans('','', '<>'))
        self.assertEqual(int_response, 'Response [200]')

        #nonInt_input --> Input from user (Non-Integer)
        #Checking... if input is non-integer
        nonInt_input = '{"value":jfahalksf}'
        json_content = requests.post(game_url, data=nonInt_input, headers=headers)
        nonInt_response = str(json_content).translate(str.maketrans('','', '<>'))
        self.assertEqual(nonInt_response, 'Response [400]')

if __name__ == '__main__':
    unittest.main()
