import requests
from requests.auth import HTTPDigestAuth


def enable_messages(ipaddrs, enable):
    username = "Push"
    password = "Push"

    url = "http://" + ipaddrs + "/api/v1/mgmt/config/set"         # API URL
    payload = "{\r\n \"data\":\r\n {\r\n \t\"apps.push.secureTunnelRequired\":\""+enable+"\",\r\n\t\"apps.push.messageType\":\"5\",\r\n\t\"apps.push.password\":\""+password+"\",\r\n\t\"apps.push.username\":\""+username+"\"\r\n }\r\n}"
    
    headers = { 'Content-Type': "application/json",
                'Authorization': 'Basic UG9seWNvbTo1MDYw',
                'Cache-Control': "no-cache",}

    response = requests.request("POST", url, headers=headers, data=payload)
    return response.status_code

def send_message(ipadd, severity, tittle, message):

    url = "http://"+ipadd+"/push"

    payload = "{\r\n \"data\":\r\n {\r\n\t  '<PolycomIPPhone><Data priority:\'"+severity+"\'><body style=\"margin: 0;padding:0;height: 100%;width: 100%;\"><div style=\"position: absolute;width: 100%;height: 100%; background-color: rgba(214, 213, 213, 0.127); margin: 0; padding: 0;\"><div style=\"width: 100%;height: 75%; margin-top: 0;\"><h1 style=\"margin: 0;\">"+tittle+"</h1><hr style=\"width: 90%; margin-left: 5%;\"><h4 style=\"margin: 0;\">"+message+"</h4></div><div style=\"width: 100%;height: 20%; background-color: #ffffff;color: #fff;\"><img style=\"height: 100%;float:right;\" src=\"https://fontslogo.com/wp-content/uploads/2017/08/Schlumberger-Logo-Font.jpg\" alt=\"\"></div></div></body></Data></PolycomIPPhone>'\r\n }\r\n}"
    
    response = requests.request("POST", url, auth=HTTPDigestAuth('Push', 'Push'), data = payload)
    
    return response

if __name__ == "__main__":
    ipaddress= '10.252.42.252'

    severity = ['All','Critical','High','Important','Normal','None']
    tittle = "Hello World!"
    message = "CX Automation student is the best!"

    msg = send_message(ipaddress, 'Critical', tittle, message)

    if (msg.status_code != 200):
        en = enable_messages(ipaddress, '0')
            
        msg = send_message(ipaddress, 'Critical', tittle, message)
    
    print(msg)