import json

import requests

headers = {
    'Content-Type': 'application/json',
}

response = requests.post('https://api.funnypay.in/callback/hiPay/payIn', headers=headers, data=json.dumps(
    {"merchantNo": "HiFP", "orderNo": "HI02208R43GSKJ", "orderId": "yXONKFjr938", "payment": "10.00",
     "userId": "917366988754", "amount": "10.00", "status": 2,
     "sign": "nj1+SeR5pXF5Pfd9jk/1NTDhcDKrrneY6DnuR2ugESRB4c90VUASrniEHgug8cIaKi4fwUgWcEPd+GjWkuqA7hxjyJpFxVHHDdUoIVXV6pfUHUyFX0k2xa51s9iNw4xI/Jjb1G1EECh4AqyDQO34hUV2RTWnWqzQFxNvxtnSE57IBvTuUSzegh50LPbE2BZM8G6V17nbsf9HiT62ziAhMyXBgHCgnGz0csB1doMUGI5UBMXEc/dFOezKSmDAoKRHuJgnDKXUoM6it5sxnhW90Vj3SSkhAexmpinFR10gyec6B7yNL6gd3qmJgW74WZFqP9z/qodCec4C/a7xcVfMpQ=="}))
print(response.text)
