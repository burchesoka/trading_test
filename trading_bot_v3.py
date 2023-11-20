import time

from trading_clients_api import check_key

if __name__ == '__main__':
    while True:
        check_key()
        time.sleep(60)
