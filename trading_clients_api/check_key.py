import requests

from settings import settings

HOST = "http://dvkotin.com:5555"


def check_key():
    retries = 2
    r = None
    while retries and not r:
        try:
            r = requests.post(
                url=HOST + '/trading_bots/check_key/',
                json={
                  "user_id": settings.user_id,
                  "secret_key": settings.user_secret_key
                }
            )
        except Exception as e:
            print('Request error')
            continue

        retries -= 1

    if r:
        print('check_key response:', r.text)
        return r.json()
    else:
        print('check_key response:', r if r is None else r.text)
        return
