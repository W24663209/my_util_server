import json

import requests


def pay_out_callback(orderNo, status):
    headers = {
        'Content-Type': 'application/json; charset=UTF-8'
    }
    url = 'https://api.funnypay.in/callback/paed/payOut'
    data = {"amount": 500, "currency": "INR", "transactionId": "OMF2314167551760169443", "pay_id": "303519236792",
            "purpose": "Salary", "reference_id": "OUT202281021900130190594335055",
            "payment_details": {"type": "bank", "account_number": "********1156", "ifsc_code": "PYTM0123456",
                                "beneficiary_name": "Naveen Bhadana", "mode": "IMPS"}, "status": "SUCCESS",
            "message": "Payout Success", "orderId": "OUT202281021900910881624657781"}
    result = requests.post(url=url, data=json.dumps(data), headers=headers)
    print(result.text)


if __name__ == '__main__':
    pay_out_callback('OUT202281021900855574254969261', 'SUCCESS')
