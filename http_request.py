# importing the requests library
import requests

# defining the api-endpoint
API_ENDPOINT = "http://cybele.ir/s.php"

# your API key here
first_name =input("Enter your firstname: ")

# your source code here
second_name= input("Enter your secondname: ")

# data to be sent to api
data = {'fname': first_name,
       'sname': second_name,
       }

# sending post request and saving response as response object
r = requests.post(url=API_ENDPOINT,data=data)

# extracting response text
print(r.text)
if r.status_code == 200:
    print('Success!')
elif r.status_code == 404:
    print('Not Found.')
#print("The pastebin URL is:%s" % pastebin_url)