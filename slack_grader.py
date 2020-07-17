import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break
    json_file = urllib.request.urlopen(address, context=ctx)
    json_data = json_file.read()
    json_list = json.loads(json_data)
    json_list = json_list['comments']
    comment_sum = 0
    for user in json_list:
        comment_sum += user['count']
    print(comment_sum)
