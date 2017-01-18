from utils import const
# 服务器地址
# adServer
const.HOST_AD_SERVER = 'http://10.9.2.10:8090'
# imServer
const.HOST_IM_SERVER = ''
# 密码加密服务器
const.HOST_ENCRYPTED_SERVER_URL = 'http://localhost:8081/passwordEncrypt/getEncryptedPWD'
const.HOST_GEN_LOGIN_KEY_URL = const.HOST_AD_SERVER + "/login/genLoginKey"
const.HOST_LOGIN_URL = const.HOST_AD_SERVER + "/login/login"
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
const.CASE_FILE_PATH = '接口测试_医生端_测试用例集.xls'

# 测试用例文件中各列说明
const.CASE_ID = 0
const.CASE_DESCRIPTION = 1
const.CASE_HTTP_METHOD = 2
const.CASE_SERVER = 3
const.CASE_HTTP_URL = 4
const.CASE_PARAMETER = 5
const.CASE_VERIFICATION_METHOD = 6
const.CASE_EXPECTED_RESULT = 7
const.CASE_PREFIX_CASE_ID = 8
const.CASE_EXECUTION = 9
const.CASE_COMMENT = 10

# 测试用例各列可选内容
const.CASE_HTTP_METHOD_POST = "post"
const.CASE_HTTP_METHOD_PUT = "put"
const.CASE_SERVER_AD_SERVER = "adServer"
const.CASE_SERVER_IM_SERVER = "aiServer"
const.CASE_VERIFICATION_METHOD_CONTAINS = "contains"
const.CASE_VERIFICATION_METHOD_EQUALS = "equals"
const.CASE_VERIFICATION_METHOD_DB = "db"
const.CASE_EXECUTION_YES = "YES"
const.CASE_EXECUTION_NO = "NO"
