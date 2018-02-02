from time import time
import random
import hashlib


# 当前时间
def get_timestamp():
    timestamp = str(time()).split('.')[0]
    return timestamp


# 微信平台的sn
def get_sn():
    sn = '563710d57a396'
    return sn


# 微信平台的key
def get_key():
    key = '9d884b9cf414fc974a824e736f850780'
    return key


# 随机10位字符
def get_nonce():
    #random_c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789abcdefghijklmnopqrstuvwxyz~!@#$%^&*()_+-='
    #nonce = ''.join(random.sample(random_c + string.digits, 10))
    nonce = 'ABCDEFGHIJ'
    return nonce


# md5生成加密密钥
def get_signature():
    timestamp = get_timestamp()
    nonce = get_nonce()
    sn = get_sn()
    key = get_key()
    # md5 signature
    md5 = hashlib.md5()
    sign_str = 'nonce=' + nonce + '&sn=' + sn + '&timestamp=' + timestamp + key
    sign_bytes_utf8 = sign_str.encode(encoding="utf-8")
    md5.update(sign_bytes_utf8)
    signature = md5.hexdigest()
    return signature
