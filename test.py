import clr
import os
clr.FindAssembly('CPUThermometerLib.dll')  # 加载c#dll文件
# print('Does this filepath exist?',os.path.isfile(file)) 
# print(clr.AddReference(file))
from  CPUThermometerLib.OpenHardwareMonitorLib import *  # 导入命名空间

