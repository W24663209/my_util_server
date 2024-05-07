import json

import curlify
import requests


def pay_out_callback(orderNo, utr, status):
    cookies = {
        'Admin-Token': 'eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjU4YTIxOWVmLTcxNzItNDMwNi04ODE4LWJmZTU5NmFjZTZkMiJ9.fM7uvki9HOqccOCpx27M9fyLBEHAFaSpUnnRTM0wrDxPetUJdJRtHng3jsfGT_5s2vLxHGpQL2MIZ6EINjvEug',
        'sidebarStatus': '0',
    }

    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Authorization': 'Bearer eyJhbGciOiJIUzUxMiJ9.eyJsb2dpbl91c2VyX2tleSI6IjU4YTIxOWVmLTcxNzItNDMwNi04ODE4LWJmZTU5NmFjZTZkMiJ9.fM7uvki9HOqccOCpx27M9fyLBEHAFaSpUnnRTM0wrDxPetUJdJRtHng3jsfGT_5s2vLxHGpQL2MIZ6EINjvEug',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json;charset=UTF-8',
        'Origin': 'https://admin.funnypay.in',
        'Pragma': 'no-cache',
        'Referer': 'https://admin.funnypay.in/order/payIn',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
    }

    data = '{"orderNo":"%s","utr":"%s","amount":"%s","status":"SUCCESS"}' % (orderNo, utr, status)

    response = requests.post('https://admin.funnypay.in/api/order/collection/cranesPayCallback', headers=headers,
                             cookies=cookies, data=data)
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    with open('../1.txt', 'r') as f:
        for text in f:
            orderNo, utr, status = text.replace('\n', '').split('\t')
            print(orderNo, utr, status)
            pay_out_callback(orderNo, utr, status)
# pay_in_callback('MAVIjZKpoGgI', 200, 'SUCCESS')
# pay_in_callback('MAVIAdd42B41', 100, 'SUCCESS')
# pay_in_callback('MAVI7h2q2lvY', 100, 'SUCCESS')
# pay_in_callback('MAVITAHZVxJV', 100, 'SUCCESS')
# pay_out_callback('OUT202281021900820065943788082', 'FAIELD')
# pay_out_callback('OUT202281021900819052872861934', 'FAIELD')
