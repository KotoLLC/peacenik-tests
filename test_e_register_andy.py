from helpers import *
     
def test_e_register_andy():
    url = "http://central.orbits.local/rpc.AuthService/Register"
    raw_payload = {"name":  "andy", "email": "andy@mail.com", "password":  "12345"}
    payload = json.dumps(raw_payload)
    headers = {'Content-Type': 'application/json'}
    
    # convert dict to json by json.dumps() for body data. 
    response = requests.request("POST", url, headers=headers, data=payload)
    save_cookies(response.cookies,"cookies.txt")
    
    # Validate response headers and body contents, e.g. status code.
    if (response.status_code == 200) or (response.status_code == 409):
        assert True
    else:
        assert False

    # print full request and response
    pretty_print_request(response.request)
    pretty_print_response(response)