import json

import requests
import re
def parse_jsonp(jsonp_str):
    try:
        return re.search('^[^(]*?\((.*)\)[^)]*$', jsonp_str).group(1)
    except:
        raise ValueError('Invalid JSONP')
headers = {
    'authority': 'cf.aliyun.com',
    'accept': '*/*',
    'accept-language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'cache-control': 'no-cache',
    'cookie': 'cna=bFJ7GzMFaUwCAXkjugsHHqDv; t=c597c5754352942ce8c9a6d55b777124; _samesite_flag_=true; cookie2=15399103f2f28d36184da7d600faba4e; _tb_token_=f497e35b90e64; _hvn_login=6; csg=74bb409e; isg=BBMTRqJadA9s5ThhmYg1n45xopE9yKeKMxXrd8UwbzJpRDPmTZg32nGVfrQqZP-C',
    'pragma': 'no-cache',
    'referer': 'https://cargonest.sal-sichuanair.com/',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'script',
    'sec-fetch-mode': 'no-cors',
    'sec-fetch-site': 'cross-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
}

params = (
    ('a', 'FFFF0N0N00000000A2D6'),
    ('t', 'FFFF0N0N00000000A2D6:nc_other:1664508949618:0.8320966935907104'),
    ('n', '223\\u0021c+CCoS7PnpygGCgyJgK6iAHGrOWIMRBFt/tSL2VflLyjURyfSxz1vmjcTp7Eith/GSpKQvDPF3fMxB/nMioctRN1FbsHpYQ0P8YYc4so2I2LxehrolTrmA++EE0s1nMvRgIOpfX56Up/ZR7y3LC1+elXzvcfpA8Z0Clwq09K18t7AzIIqm8sh/tcnfb98Kv/a/BZwehPTvwwErInxsHs7OL3YdIerER404KH0ktk2yQyEEmYDJlMjUMtMs38IZiOI0aqxAWs3ydUx4jkqoluJ/El8/pp/BeujC3o0uLQDy06nZ8ne2DqflYj8RINTspzzQ9QTbUTB/HFFKPmdjiX6m3JvMyWWCQosjiMXaPSbj2SH4EuFirKUC4Ir/LnbOmvggYNDDIi6renIjjrPavnwnWuhDAIX8l80XVLlH5d5fLqes2kD2D3TKeC8/CZlra1vvIZa3Z35UAXsJ/buu2lDdcWyFxXIZjwhmdXXyErelEqvuPfLkSyjuZxkOskdskJuVk7odqNFJiyhWmRkq2LqzgV5T8noAFqKmnviMa417/OWTQ+VJmbcotHgXuFTcl6mDGNKJCkPKcRrUkT8iYzaS5lbq1th22kfvyKpkut6qZaCjyS7efhWPu3apSalHrJ84ZZWfqaku5FvRb5JAxWFGiwfMvr1ItcQD/1o/chX3FJh/i8ALr+CV7iEUaMev5s5nXxE74Pe21wICHVvAVv+ZSvUTa8VT8d9cTx69/0bbABEJtLb0wyDGWVJB5mSXOgJJ0iGzcQlDTU1HkU++C2PHaB/zJcN5xD88xOFMXKZ7WI6GelAGsZwPemAb6mqR2qIU5vOcDcnbKGbglDmVefnRefSvMypVuoUPNJcyLA7PeGVzfyRo9zh+N4/YCdOTFhcI3dft045O+0jtqmCeE1GUNXgmeHJ2ce+D4+x9EeF9L8hfibWlnpgH6PqWCS+csxDj09cRcPnbbrO+ck+tsXZO4R2+5dkPP0DGbBk6jznaZRijCbnw46UZ93+fEefkRSIrxOB0KnVGFhEvpAFGTQgIGP8iyWorQmKkf1V7ruGBhMleKrfcBMsmuLoMgIJ01Q5blobDM/P6cRDHVMmDGe+7w0Pnmem7eyERZG7oqB+OStyhbaM2nfC0bS9543nK2vBYAF/s0ZShSY3g7LipCw0QQwvu242in9M7xg2ZYUkAEZsIRA65u1sVkjZFC6YNafHsh1mGI6RxYzauKaG0kz3sIvrSXvyAKcX5o+WRMgHNmSs2wanIUPKxu6UD6NWGKLBnSWSQrkfQsIWZgqQ2usWMmsDrPNGvbrHnVNgbHy+1lGcQQ4z3c/eW3JcQXCWGh/rQR4iGwQSrXS1OyTcLR3LHySiOg1mc3w0ujTQjzr4aWL15m4w4um10Mvi5z46aQRSr2Jzj6jSUl4cEC4ZJGv+I34Tjx28wd+IWSXciwqw1TpcwCyd9U/eg34cQbhdOw9xjRycAcqe1C4rCpyzJHg+g31ACQCWGh/rWbXc/ugqWcMtIZEPpPa1jy6eGMFbHlw21a+700SYE64M/pdPjnjhttUVn2FQujSS5DFpAcEedA558beQh45GyUo9EcsR0kXp0O9sdSEjGEvPmvdz3vf7XywxPivmbvUd7Rp/m3J59vGxyTtNptXOA9EvtBXX1kU5cJJQg07eYTpBaFXdoahACNIitUEMmKByIOjOs5AxWuNg+kKNxLtyiifeugeYlnmYFhhk40HZO2ZAGyo8GBlRTZmwT2TUOej3AVWm1ywRFF4J/o54fhxPnTohqhjE8jVJjpZ29EB8Q7umGFszU7uWWbJt56LzHFgxXyzpL6Rf2AhnhKnRpw/p0yGycNWvHurXOSsiYzNS/BWl0BcY+H1diNlrgfBbYcShBSxjtdeeFjANG7HOZ6iFoaSyTvkE89GisGX8wwba+gSfdwaE47jeuh/xZXSTNmpCuuw3WP+VYaCeSlkscEFxsgVETKps2VEr3IF4kwhoBENuWk9AQeoOadfuxbsYZzcUHHi1g1lRfLtusqWbwb+qJSZssCcRBF4bvp4vw3F80gHmlnD5XgGKC7Xs7Z9XWlSKoAJEybaNe8xy6ldmxEvLo7cje7JlLqawkTwe9ZI4dqZ399oNEwNTMXtpWE0VTNXCt+eCzpNNXO1oKfBXWjZ12nlNdNsD4l4PM4uY0+/htBf7sFcts/bnYou1pU8rg3Swj94lOdCrIQv8wdNdzAy6dhqA4TTuAwpjKbDy82R1kuYCXOLGTOCVKpisSjYlwwQQXdZWS6WecPqMPGjRasem/s9pAk0dLvSn6krD8gi7SXcg/XVXKUCpwayFwZT+6t8yQj+RY4j3pvCvEAqPPRFvhO8ltaZoZHzIfNkLfyLyFyWi97GZEmcLnW80GoXmkdoRVTfCCOcnCNzHAd2UFBntZ53m+5FEBs1FCkU5xVLOeZPGC1KlVjJHzdlfUCl7Pf0x7dAKoL/jjQdxRp3mI39rqi1VWdFvncfasvbiU3cQjNkPUSmdwBtdPPy4wZtSlp7KGvOilE5j2esjhgeUt7JfYPBfd+zw6IVuX2otBuUTRSWI42jn4Q5tBi1OcbvgkHwbosgxUo3nE67oI299TpRO0DI9dkDWvidPUTwWHoJaaPtxgYoJ/pW0ja0g6Fxb/nEvb2conE5ORlITVmZV1SBNurTMpGFSIE7OW0pXxWNMGb1QK5GrqwyeKJybbW5d8X6i9MOglJ7cUha8iIyfQHuqj=='),
    ('p', '{"umidToken":"G2E6E35567438E24762CFF5E3C05A3BBD03D622D5B1021A62BA","ncSessionID":"895d43a54eb"}'),
    ('scene', 'nc_other'),
    ('asyn', '0'),
    ('lang', 'cn'),
    ('v', '1'),
    ('callback', 'jsonp_04712852305848294'),
)

response = requests.get('https://cf.aliyun.com/nocaptcha/analyze.jsonp', headers=headers, params=params)
print(json.loads(parse_jsonp(response.text))['result']['value'])
exit()

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json; charset=UTF-8',
    'Origin': 'https://cargonest.sal-sichuanair.com',
    'Pragma': 'no-cache',
    'Referer': 'https://cargonest.sal-sichuanair.com/processTracking',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
    'lang': 'null',
    'ncToken': 'FFFF0N0N00000000A2D6:nc_other:1664508949618:0.8320966935907104',
    'sec-ch-ua': '"Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sessionId': '016hfsmv0QGlc0XrbioumoMQq4tW3lhfvRjTXuxMGKX0bM4HnmPwyBlR1atskxS-G9FDmeaalRXu3FBFhK5g0DiTmmZzerqkc6o7g8fEfO5Yvq4TlDfmNlfLg7enZ6KKD5k5lCYS6rcsz1DVrUEvrn5vku9zXRE78s3uxX0NmrBy-bT04nnG3X66wYe_N4B9ug9DZ6R1TYdPQeOfZKWkJwYQ',
    'sig': '05XBa8EtGVqtX0rzvVYJMIN5Nt3ymio7agdvP1_Lee617UpsidkA8kGPJe611XXhjAnDWg22l8bC-npV6FKoU6wnzLVxWfkw8YXWEFDJoC_25n2RjCRR6didQ4htyAAMES7xPSOEIKBjiQR0y0ME7xbr86Rr0S1sY5rK8v9tjgA866Lcj9YE4fdMuncbza4pm237Yo-Q_whsOJKPlfAbcuCgi8jmoN28lFDu6q_yXRSVNRtF21YB2aoDBkKde-6RA8ARcqnMRC5Jvx0hErKBK59Zk7i9mm43NcqgYF6f8HuF4yrnZJ1eaH4_JQcus1AKktBCIMG3hig32ZfMk5sfUc4jPPjMNtdwHW8bZUa2WrU1KHIF5qe8hQl754E3BrTaDwsGbnhSUTqrIB2wY2W3WEesakh35kzvD9W3nQf630kjB46gj0xiOLxQFp1073g4pIiAqYwHOfjmtWMHs2EQi69eVNHogkcZssAVxJADStsoDY94r_LXIIil3Y3aVPRGAe',
    'terminalType': '1',
    'token': 'null',
}

data = '{"t":1664509116511,"terminalType":"1","waybillPre":"31313131","waybillno":"131231","language":"chinese"}'

response = requests.post('https://cargonest.sal-sichuanair.com:60060/open/api-xcbz/processTracking/getProcessTrackingForApi', headers=headers, data=data)

#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://cf.aliyun.com/nocaptcha/analyze.jsonp?a=FFFF0N0N00000000A2D6&t=FFFF0N0N00000000A2D6%3Anc_other%3A1664508949618%3A0.8320966935907104&n=223\u0021c%2BCCoS7PnpygGCgyJgK6iAHGrOWIMRBFt%2FtSL2VflLyjURyfSxz1vmjcTp7Eith%2FGSpKQvDPF3fMxB%2FnMioctRN1FbsHpYQ0P8YYc4so2I2LxehrolTrmA%2B%2BEE0s1nMvRgIOpfX56Up%2FZR7y3LC1%2BelXzvcfpA8Z0Clwq09K18t7AzIIqm8sh%2Ftcnfb98Kv%2Fa%2FBZwehPTvwwErInxsHs7OL3YdIerER404KH0ktk2yQyEEmYDJlMjUMtMs38IZiOI0aqxAWs3ydUx4jkqoluJ%2FEl8%2Fpp%2FBeujC3o0uLQDy06nZ8ne2DqflYj8RINTspzzQ9QTbUTB%2FHFFKPmdjiX6m3JvMyWWCQosjiMXaPSbj2SH4EuFirKUC4Ir%2FLnbOmvggYNDDIi6renIjjrPavnwnWuhDAIX8l80XVLlH5d5fLqes2kD2D3TKeC8%2FCZlra1vvIZa3Z35UAXsJ%2Fbuu2lDdcWyFxXIZjwhmdXXyErelEqvuPfLkSyjuZxkOskdskJuVk7odqNFJiyhWmRkq2LqzgV5T8noAFqKmnviMa417%2FOWTQ%2BVJmbcotHgXuFTcl6mDGNKJCkPKcRrUkT8iYzaS5lbq1th22kfvyKpkut6qZaCjyS7efhWPu3apSalHrJ84ZZWfqaku5FvRb5JAxWFGiwfMvr1ItcQD%2F1o%2FchX3FJh%2Fi8ALr%2BCV7iEUaMev5s5nXxE74Pe21wICHVvAVv%2BZSvUTa8VT8d9cTx69%2F0bbABEJtLb0wyDGWVJB5mSXOgJJ0iGzcQlDTU1HkU%2B%2BC2PHaB%2FzJcN5xD88xOFMXKZ7WI6GelAGsZwPemAb6mqR2qIU5vOcDcnbKGbglDmVefnRefSvMypVuoUPNJcyLA7PeGVzfyRo9zh%2BN4%2FYCdOTFhcI3dft045O%2B0jtqmCeE1GUNXgmeHJ2ce%2BD4%2Bx9EeF9L8hfibWlnpgH6PqWCS%2BcsxDj09cRcPnbbrO%2Bck%2BtsXZO4R2%2B5dkPP0DGbBk6jznaZRijCbnw46UZ93%2BfEefkRSIrxOB0KnVGFhEvpAFGTQgIGP8iyWorQmKkf1V7ruGBhMleKrfcBMsmuLoMgIJ01Q5blobDM%2FP6cRDHVMmDGe%2B7w0Pnmem7eyERZG7oqB%2BOStyhbaM2nfC0bS9543nK2vBYAF%2Fs0ZShSY3g7LipCw0QQwvu242in9M7xg2ZYUkAEZsIRA65u1sVkjZFC6YNafHsh1mGI6RxYzauKaG0kz3sIvrSXvyAKcX5o%2BWRMgHNmSs2wanIUPKxu6UD6NWGKLBnSWSQrkfQsIWZgqQ2usWMmsDrPNGvbrHnVNgbHy%2B1lGcQQ4z3c%2FeW3JcQXCWGh%2FrQR4iGwQSrXS1OyTcLR3LHySiOg1mc3w0ujTQjzr4aWL15m4w4um10Mvi5z46aQRSr2Jzj6jSUl4cEC4ZJGv%2BI34Tjx28wd%2BIWSXciwqw1TpcwCyd9U%2Feg34cQbhdOw9xjRycAcqe1C4rCpyzJHg%2Bg31ACQCWGh%2FrWbXc%2FugqWcMtIZEPpPa1jy6eGMFbHlw21a%2B700SYE64M%2FpdPjnjhttUVn2FQujSS5DFpAcEedA558beQh45GyUo9EcsR0kXp0O9sdSEjGEvPmvdz3vf7XywxPivmbvUd7Rp%2Fm3J59vGxyTtNptXOA9EvtBXX1kU5cJJQg07eYTpBaFXdoahACNIitUEMmKByIOjOs5AxWuNg%2BkKNxLtyiifeugeYlnmYFhhk40HZO2ZAGyo8GBlRTZmwT2TUOej3AVWm1ywRFF4J%2Fo54fhxPnTohqhjE8jVJjpZ29EB8Q7umGFszU7uWWbJt56LzHFgxXyzpL6Rf2AhnhKnRpw%2Fp0yGycNWvHurXOSsiYzNS%2FBWl0BcY%2BH1diNlrgfBbYcShBSxjtdeeFjANG7HOZ6iFoaSyTvkE89GisGX8wwba%2BgSfdwaE47jeuh%2FxZXSTNmpCuuw3WP%2BVYaCeSlkscEFxsgVETKps2VEr3IF4kwhoBENuWk9AQeoOadfuxbsYZzcUHHi1g1lRfLtusqWbwb%2BqJSZssCcRBF4bvp4vw3F80gHmlnD5XgGKC7Xs7Z9XWlSKoAJEybaNe8xy6ldmxEvLo7cje7JlLqawkTwe9ZI4dqZ399oNEwNTMXtpWE0VTNXCt%2BeCzpNNXO1oKfBXWjZ12nlNdNsD4l4PM4uY0%2B%2FhtBf7sFcts%2FbnYou1pU8rg3Swj94lOdCrIQv8wdNdzAy6dhqA4TTuAwpjKbDy82R1kuYCXOLGTOCVKpisSjYlwwQQXdZWS6WecPqMPGjRasem%2Fs9pAk0dLvSn6krD8gi7SXcg%2FXVXKUCpwayFwZT%2B6t8yQj%2BRY4j3pvCvEAqPPRFvhO8ltaZoZHzIfNkLfyLyFyWi97GZEmcLnW80GoXmkdoRVTfCCOcnCNzHAd2UFBntZ53m%2B5FEBs1FCkU5xVLOeZPGC1KlVjJHzdlfUCl7Pf0x7dAKoL%2FjjQdxRp3mI39rqi1VWdFvncfasvbiU3cQjNkPUSmdwBtdPPy4wZtSlp7KGvOilE5j2esjhgeUt7JfYPBfd%2Bzw6IVuX2otBuUTRSWI42jn4Q5tBi1OcbvgkHwbosgxUo3nE67oI299TpRO0DI9dkDWvidPUTwWHoJaaPtxgYoJ%2FpW0ja0g6Fxb%2FnEvb2conE5ORlITVmZV1SBNurTMpGFSIE7OW0pXxWNMGb1QK5GrqwyeKJybbW5d8X6i9MOglJ7cUha8iIyfQHuqj%3D%3D&p=%7B%22umidToken%22%3A%22G2E6E35567438E24762CFF5E3C05A3BBD03D622D5B1021A62BA%22%2C%22ncSessionID%22%3A%22895d43a54eb%22%7D&scene=nc_other&asyn=0&lang=cn&v=1&callback=jsonp_04712852305848294', headers=headers)
