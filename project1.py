import sys
import requests
import socket
import json

if len(sys.argv) < 2:
    printf("Usage : " + sys.argv[0] + " < url>")
    sys.exit(1)

req = requests.get("https://" + sys.argv[1])
print("\n" + str(req.headers))

ip_address = socket.gethostbyname(sys.argv[1])
print("\nThe Ip address of " + sys.argv[1] + " is: " + ip_address + "\n")

req_two = requests.get("https://ipinfo.io/" + ip_address + "/json")
print(req_two.text)
resp_ = json.loads(req_two.text)

print("Internal Hostname : " + resp_['hostname'])
print("Location : " + resp_['loc'])
print("City : " +resp_['city'])
print("Region : " +resp_['region'])
print("Country : " +resp_['country'])
print("Post Code : " +resp_['postal'])
print("Owner Organisation : " +resp_['org'])
print("Timezone : " +resp_['timezone'])
