import js2py
with open('test.js', 'r', encoding='UTF-8') as f:
    js_code = f.read()
context = js2py.EvalJs()
context.execute(js_code)
def callback(msg):
    print(msg)

result = context.qrDecode("/Users/weizongtang/Downloads/https___payzing.in_user_setting.png",callback)
print(result)