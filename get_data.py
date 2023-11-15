import requests
import json
import schedule
from time import sleep
import asyncio
import random

proxy_list = [
    "103.59.170.135:9982:ztech:Ztech@223999",
    "103.59.170.176:9982:ztech:Ztech@223999",
    "103.59.170.175:9982:ztech:Ztech@223999",
    "103.59.170.145:9982:ztech:Ztech@223999",
    "103.59.170.184:9982:ztech:Ztech@223999",
    "103.59.170.183:9982:ztech:Ztech@223999",
    "103.59.170.182:9982:ztech:Ztech@223999",
    "103.59.170.181:9982:ztech:Ztech@223999",
    "103.59.170.180:9982:ztech:Ztech@223999",
    "103.59.170.179:9982:ztech:Ztech@223999",
    "103.59.170.178:9982:ztech:Ztech@223999",
    "103.59.170.177:9982:ztech:Ztech@223999",
    "103.59.170.189:9982:ztech:Ztech@223999",
    "103.59.170.136:9982:ztech:Ztech@223999",
    "103.59.170.134:9982:ztech:Ztech@223999",
    "103.59.170.138:9982:ztech:Ztech@223999",
    "103.59.170.139:9982:ztech:Ztech@223999",
    "103.59.170.137:9982:ztech:Ztech@223999",
    "103.59.170.141:9982:ztech:Ztech@223999",
    "103.59.170.142:9982:ztech:Ztech@223999",
    "103.59.170.202:9982:ztech:Ztech@223999",
]

def get_lottery_data(api_url):
    proxy = random.choice(proxy_list)
    proxy = proxy.strip().split(":")
    proxy_address = proxy[0]
    proxy_port = proxy[1]
    proxy_username = proxy[2]
    proxy_password = proxy[3]

    proxies = {
        'http': f'http://{proxy_username}:{proxy_password}@{proxy_address}:{proxy_port}'
    }

    response = requests.get(api_url, proxies=proxies)

    if response.status_code == 200:
        data_get = response.json()
        code = data_get["data"]["code"]
        begin_time = data_get["data"]["begin_time"]
        last_issue = data_get["data"]["last_issue"]
        open_numbers_formatted = data_get["data"]["open_numbers_formatted"]
        official_time = data_get["data"]["official_time"]
        return code, begin_time, last_issue, open_numbers_formatted, official_time
    else:
        print("GET request không thành công. Mã trạng thái:", response.status_code)
        return None, None, None, None, None

def post_lottery_data(url, data):
    json_data = json.dumps(data)

    headers = {
        'Content-Type': 'application/json',
        'accept': 'application/json'
    }

    response = requests.post(url, headers=headers, data=json_data)

    if response.status_code == 200:
        print("POST request thành công!")
        print("Phản hồi từ máy chủ:")
        print(response.json())
    else:
        print("POST request không thành công!")
        print("Mã trạng thái:", response.status_code)


async def main():
    await asyncio.sleep(20)
    api_url = "https://luck8882.com/server/lottery/getCurrentLotteryInfo?lottery_id=49"
    code, begin_time, last_issue, open_numbers_formatted, official_time = get_lottery_data(api_url)

    if code is not None:
        data_post = {
            "code": code,
            "begin_time": begin_time,
            "open_numbers_formatted": open_numbers_formatted,
            "issue": last_issue,
            "official_time": official_time
        }

        post_url = 'http://123.30.234.209:8080/l33/'
        post_lottery_data(post_url, data_post)

def run_main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())

schedule.every().hour.at(":00").do(run_main)
schedule.every().hour.at(":02").do(run_main)
schedule.every().hour.at(":04").do(run_main)
schedule.every().hour.at(":06").do(run_main)
schedule.every().hour.at(":08").do(run_main)
schedule.every().hour.at(":10").do(run_main)
schedule.every().hour.at(":12").do(run_main)
schedule.every().hour.at(":14").do(run_main)
schedule.every().hour.at(":16").do(run_main)
schedule.every().hour.at(":18").do(run_main)
schedule.every().hour.at(":20").do(run_main)
schedule.every().hour.at(":22").do(run_main)
schedule.every().hour.at(":24").do(run_main)
schedule.every().hour.at(":26").do(run_main)
schedule.every().hour.at(":28").do(run_main)
schedule.every().hour.at(":30").do(run_main)
schedule.every().hour.at(":32").do(run_main)
schedule.every().hour.at(":34").do(run_main)
schedule.every().hour.at(":36").do(run_main)
schedule.every().hour.at(":38").do(run_main)
schedule.every().hour.at(":40").do(run_main)
schedule.every().hour.at(":42").do(run_main)
schedule.every().hour.at(":44").do(run_main)
schedule.every().hour.at(":46").do(run_main)
schedule.every().hour.at(":48").do(run_main)
schedule.every().hour.at(":50").do(run_main)
schedule.every().hour.at(":52").do(run_main)
schedule.every().hour.at(":54").do(run_main)
schedule.every().hour.at(":56").do(run_main)
schedule.every().hour.at(":58").do(run_main)


while True:
    schedule.run_pending()
    sleep(1)
