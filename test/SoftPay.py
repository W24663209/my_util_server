import requests
text='OUT202281021900891370194560901'
response = requests.get('https://api.funnypay.in/api/queryPayOut?sign=000000WW&orderNo=%s' % text.replace('\n', ''))
print(text, response.text)

# 1245777469
# 1245777502
# 1245777514
