import httplib2
import json
import random
import time
import datetime
import sys

if __name__ == '__main__':
    httplib2.debuglevel     = 0
    http                    = httplib2.Http()
    content_type_header     = "application/json"
    game_url = "http://127.0.0.1:5000/guess"

    #Reads the server URL and access the response from server
    index_url = "http://127.0.0.1:5000/"
    response= json.loads(http.request(index_url)[1])
    print(response)

def start():
    while True:
        
		try:
            user_input = int(input("Enter Number: "))
            headers = {'Content-Type': content_type_header}
            data = {'value': user_input}
            #client posts data to the server; http request and json response
            response, content = http.request(game_url,'POST',json.dumps(data),headers=headers)
            json_object = json.loads(content)
            print (content)
        except ValueError:
            print("Only Integers allowed!")
            continue
        
		#If the user guess is correct then program terminates
        #otherwise it asks for user input
        for element in json_object['answer'][0]:
            if element == "T":
                continue
            else:
                sys.exit(0)
start()
