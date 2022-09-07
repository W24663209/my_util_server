# const val RSSI_1M: Double = 50.0//发射端和接收端相隔1米时的信号强度
# const val N_VALUE: Double = 2.5//环境衰减因子
#
# /**
#  * 根据rssi值估算出距离
#  * @param rssi信号强度
#  * @return 距离(单位：米)
#  */
# fun getDistance(rssi: Int): Double {
#     val rssiAbs = Math.abs(rssi)
#     val power = (rssiAbs - RSSI_1M) / (10 * N_VALUE)
#     return Math.pow(10.0, power)
# }
import math

RSSI_1M = 50.0
N_VALUE = 2.5

def getDistance(rssi):
    rssiAbs = math.fabs(rssi)
    power = (rssiAbs - RSSI_1M) / (10 * N_VALUE)
    return math.pow(10.0,power)

print(getDistance(-68.006000))