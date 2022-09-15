import requests

headers = {
    'Host': 'parkinglockapi.weirui0755.com',
    'Connection': 'close',
    'charset': 'utf-8',
    'ticket': '6F35F037FABB41509DA391C4C0C1EE34',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 11; ONEPLUS A6000 Build/RKQ1.201217.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/4309 MMWEBSDK/20220604 Mobile Safari/537.36 MMWEBID/7899 MicroMessenger/8.0.24.2180(0x28001851) WeChat/arm64 Weixin NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'content-type': 'application/x-www-form-urlencoded',
    'Accept-Encoding': 'gzip, deflate',
    'Referer': 'https://servicewechat.com/wx68b26f60a0b5f3be/0/page-frame.html',
}

params = (
    ('name', ''),
    ('lngY', '113.89340277777778'),
    ('latX', '22.562509765625'),
    ('pageNum', '1'),
    ('pageSize', '10'),
)

response = requests.get('https://parkinglockapi.weirui0755.com/1001/pk/parking/PkParkingInfo/list', headers=headers, params=params, verify=False)
print(response.text)
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://parkinglockapi.weirui0755.com/1001/pk/parking/PkParkingInfo/list?name=&lngY=113.89340277777778&latX=22.562509765625&pageNum=1&pageSize=10', headers=headers, verify=False)
