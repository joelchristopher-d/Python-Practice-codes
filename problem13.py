

# checking the server is down or good for websites


import requests

def instagram():
    url= "https://www.instagram.com/"
#     url= "https://account.ineuron.ai/signin?domain=learn.ineuron.ai&redirectUrl=/"
    response = requests.get(url)
    return response.status_code != 200
if __name__ == "__main__":
    if instagram():
        print("down")
    else:
        print("up")