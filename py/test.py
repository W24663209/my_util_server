import requests

headers = {
    'authority': 'post.iq',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundary9DzaGUbFmU2hOrwH',
    'origin': 'https://post.iq',
    'pragma': 'no-cache',
    'referer': 'https://post.iq/en/%d8%aa%d8%aa%d8%a8%d8%b9-%d8%a7%d9%84%d8%b4%d8%ad%d9%86%d8%a9/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

data = '------WebKitFormBoundary9DzaGUbFmU2hOrwH\r\nContent-Disposition: form-data; name="security"\r\n\r\n646878b213\r\n------WebKitFormBoundary9DzaGUbFmU2hOrwH\r\nContent-Disposition: form-data; name="_wp_http_referer"\r\n\r\n/en/%d8%aa%d8%aa%d8%a8%d8%b9-%d8%a7%d9%84%d8%b4%d8%ad%d9%86%d8%a9/\r\n------WebKitFormBoundary9DzaGUbFmU2hOrwH\r\nContent-Disposition: form-data; name="action"\r\n\r\nbarcode\r\n------WebKitFormBoundary9DzaGUbFmU2hOrwH\r\nContent-Disposition: form-data; name="tBarcode"\r\n\r\nCP286047878IQ\r\n------WebKitFormBoundary9DzaGUbFmU2hOrwH--\r\n'


response = requests.post('https://post.iq/wp-admin/admin-ajax.php', headers=headers, data=data.encode('utf-8'))
print(response.text)
