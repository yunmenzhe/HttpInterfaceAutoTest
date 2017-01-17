from utils import const
# 服务器地址
# adServer
const.HOST_ADSERVER = 'http://10.9.2.10:8090'
# imServer
const.HOST_IMSERVER = ''
# 密码加密服务器
const.HOST_ENCRYPTEDSERVER = 'http://localhost:8081'

# 医生账户
const.DOCTOR_PHONE = '13811984643'
const.DOCTOR_PWD = '123456'

# 默认HTTP Header
const.DEFAULT_HEADER = {
    '_m': "90:67:1c:cc:98:2c",  # 设备的MAC地址
    '_p': "1",  # 平台 1：Andorid / 2：iphone/ 3:weixin
    '_v': "2.6.6",  # 客户端版本号
    'userType': "d"  # 账户类型
}

# 设备号 deviceSN
const.DEVICE_SN = 'F2LR36GCGRWM'

# 测试用例文件路径

const.TESTCASE_FILE_PATH = '接口测试_医生端_测试用例集.xls'
