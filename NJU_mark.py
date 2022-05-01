import random

from loguru import logger

from njupass import NjuUiaAuth
from report import apply

candidate_locations = [
    '中国江苏省南京市栖霞区金大路',
    '中国江苏省南京市栖霞区九乡河东路',
    '中国江苏省南京市栖霞区仙林大道163号南京大学',
    '江苏省南京市栖霞区九乡河东路157号',
]


def login(username, password, logger, auth: NjuUiaAuth):
    """
    登录统一验证
    :return True 如果登录成功
    """
    logger.info('尝试登录...')

    if auth.needCaptcha(username):
        logger.info("统一认证平台需要输入验证码才能继续，尝试识别验证码...")
    ok = auth.tryLogin(username, password)
    if not ok:
        logger.error("登录失败。可能是用户名或密码错误，或是验证码无法识别。")
        return False

    logger.info('登录成功！')
    return True


def mark(username, password, location):
    assert username and password

    auth = NjuUiaAuth()
    method = 'YESTERDAY'

    if not location or location.lower() == 'none':
        location = random.choice(candidate_locations)

    # try to login
    ok = login(username, password, logger, auth)
    if not ok:
        return False

    # start reporting
    ok = apply(location, logger, auth)
    if not ok:
        return False

    return True
