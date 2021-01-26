from helpers import *
     
def test_c_login_matt():
    url = "http://central.orbits.local/rpc.AuthService/Login"
    raw_payload = {"name": "matt","password": "12345"}
    payload = json.dumps(raw_payload)
    headers = {'Content-Type': 'application/json'}

    
    # convert dict to json by json.dumps() for body data. 
    response = requests.request("POST", url, headers=headers, data=payload)
    save_cookies(response.cookies,"cookies.txt")
    
    # Validate response headers and body contents, e.g. status code.
    assert response.status_code == 200

    # print full request and response
    pretty_print_request(response.request)
    pretty_print_response(response)