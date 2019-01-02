import requests
import json
BASE_URL='https://api.sandbox.paypal.com/'
# ENDPOINT='cricket/'
# access_token$sandbox$ggk7dgft7jwf2kk2$ebb7d518a8e354afaf1dcae76f10b443
# shashank.ragireddy-facilitator_api1.gmail.com
# PASSWORD HDCL8TDRUPGHAEB4
# Signature AgVp3S42ue1sslkh-skgWYaRnX6sAQr78PINyC5TLcE2iz-KI5ILQqFk
# access_token$sandbox$q52n8hp6hcj5352x$b8c3774d5e8deb3abf564de7a80e7c40
ENDPOINT='v1/payments/payment/'
# BEARER_TOKEN = 'EDRFJf_9d9ra68Gw7NQMqQ0lBF61Swm88502TpCahtkO-Iqz5WBCJyCxc-VlM3zyeHOgN_YlBrM8Yewd'
# BEARER_TOKEN = 'EF-Dun8tOIrid29PfT-QsDH9dVSdIpx5-eKtE357Lb2U_sjxNClLQ7Th4kOBznfksuMQxzJhG0XZI3lW'
BEARER_TOKEN = 'A21AAGQpBJ6qBf482BAJkQ1Kw_kXACjknZYvDTbQmn5SvsZ2Otn9tq1INMl2dL1Vv9zwQzkm5Pb_XEKPfBvWhBBGVpuyp7hEA'

print(BEARER_TOKEN)
def create_payment():

    headers = {'content-type': 'application/json','Authorization': 'Bearer ' + BEARER_TOKEN  }

    data = {
      "intent": "sale",
      "payer": {
        "payment_method": "paypal"
      },
      "transactions": [
        {
          "amount": {
            "total": "30.11",
            "currency": "USD",
            "details": {
              "subtotal": "30.00",
              "tax": "0.07",
              "shipping": "0.03",
              "handling_fee": "1.00",
              "shipping_discount": "-1.00",
              "insurance": "0.01"
            }
          },
          "description": "The payment transaction description.",
          "custom": "EBAY_EMS_90048630024435",
          "invoice_number": "48787589673",
          "payment_options": {
            "allowed_payment_method": "INSTANT_FUNDING_SOURCE"
          },
          "soft_descriptor": "ECHI5786786",
          "item_list": {
            "items": [
              {
                "name": "hat",
                "description": "Brown hat.",
                "quantity": "5",
                "price": "3",
                "tax": "0.01",
                "sku": "1",
                "currency": "USD"
              },
              {
                "name": "handbag",
                "description": "Black handbag.",
                "quantity": "1",
                "price": "15",
                "tax": "0.02",
                "sku": "product34",
                "currency": "USD"
              }
            ],
            "shipping_address": {
              "recipient_name": "Brian Robinson",
              "line1": "4th Floor",
              "line2": "Unit #34",
              "city": "San Jose",
              "country_code": "US",
              "postal_code": "95131",
              "phone": "011862212345678",
              "state": "CA"
            }
          }
        }
      ],
      "note_to_payer": "Contact us for any questions on your order.",
      "redirect_urls": {
        "return_url": "https://example.com/return",
        "cancel_url": "https://example.com/cancel"
      }
    }
    resp = requests.post(BASE_URL+ENDPOINT,headers=headers,data=json.dumps(data))
    print(resp.status_code)
    print(resp.json())

create_payment()
