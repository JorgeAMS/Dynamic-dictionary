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

    payload = "{\r\n \"data\":\r\n {\r\n\t  '<PolycomIPPhone><Data priority:\\'"+severity+"\\'> <h1>"+tittle+"</h1> "+message+"</Data></PolycomIPPhone>'\r\n }\r\n}"
    payload = "{\r\n \"data\":\r\n {\r\n\t  '<PolycomIPPhone><Data priority:\\'"+severity+"\\'> <?php echo 'Hello AMS!' ?> </Data></PolycomIPPhone>'\r\n }\r\n}"
    
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