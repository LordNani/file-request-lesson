import requests
from requests.auth import HTTPBasicAuth
# Press the green button in the gutter to run the script.
if name == 'main':
    # response = requests.get('http://api.open-notify.org/astros.json')
    # print(response.json())

    # query = {'lat' : '45', 'lon' : '180'}
    # response = requests.get('http://api.open-notify.org/iss-pass.json', query)
    # print(response.json())

    response = requests.post('https://httpbin.org/post', data={'key': 'value'})
    if (response.status_code == 200):
        print(response)
        print(response.json())
    else:
        print('Request failed')


    response = requests.put('https://httpbin.org/put', data={'key': 'value'})
    print(response)
    print(response.json())
    print(response.headers['date'])

    response = requests.get('https://api.github.com/user',auth=HTTPBasicAuth('username', 'password'))
    print(response)

    my_headers = {'Authorization': 'Bearer {access_token}'}
    response = requests.get('http://httpbin.org/headers', headers=my_headers)