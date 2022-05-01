from NJU_mark import mark
import time
import json
from loguru import logger

if __name__ == '__main__':
    while True:
        with open('./users.json', 'r') as f:
            users = json.load(f)

        for user, attributes in users.items():
            username, password, location = attributes
            for i in range(10):
                logger.info(f"[{user}]尝试第[{i+1}]次打卡")
                try:
                    if mark(*attributes):
                        break
                except:
                    pass
        time.sleep(10800)

    # try:
    #     success = mark('config.ini')
    #     if success:
    #         print("打卡成功！")
    #     else:
    #         print("打卡失败！")
    # except Exception as e:
    #     print("打卡失败，原因："  + str(e))
