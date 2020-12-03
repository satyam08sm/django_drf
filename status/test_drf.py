import requests
import os
import json

ENDPOINT = "http://127.0.0.1:8000/"
image_path = os.path.join(os.getcwd(), "sample_ss.jpg")
AUTH_ENDPOINT = ENDPOINT + 'api/token/'
REFRESH_ENDPOINT = AUTH_ENDPOINT + 'refresh/'

data = {
    'username': 'satyam',
    'password': '123456',
}
headers = {
    'content-type': 'application/json'
}
r = requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
access_token = r.json()['access']
refresh_token = r.json()['refresh']
# print(r.json())

p_data = {"content": "put2 - new data auth"}
post_data = json.dumps(p_data)
post_headers = {
    # 'content-type': 'application/json',
    'Authorization': "Bearer " + access_token
}

with open(image_path, 'rb') as image:
    file_data = {
        'image': image
    }
    post_response = requests.put(ENDPOINT + str(7) + "/", headers=post_headers, files=file_data)

print(post_response.text)

# refresh_data = {
#     'refresh': refresh_token,
# }
#
# # print(type(access_token))
#
# refresh_req = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
#
# print(refresh_req.json())

################################

# get_endpoint = ENDPOINT + str(1)

#
# r = requests.get(get_endpoint)
# print(r.text)
#
# r2 = requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers = {
#     'content-type': 'application/json'
# }
# post_response = requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)


def do(method='get', data={}, is_json=True):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r


# do()


def do_img(method='get', data={}, is_json=True, img_path=None):
    headers = {}
    if is_json:
        headers['content-type'] = 'application/json'
        data = json.dumps(data)
    if img_path is not None:
        with open(image_path, 'rb') as image:
            file_data = {
                'image': image
            }
            r = requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)

    else:
        r = requests.request(method, ENDPOINT, data=data, headers=headers)
    print(r.text)
    print(r.status_code)
    return r

# do_img(method='post', data={'user': 1, 'content': ""}, is_json=False, img_path=image_path)
