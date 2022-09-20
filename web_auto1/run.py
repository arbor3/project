import unittest
# 由于python执行的时候需要根据sys.path下能扫描到的包进行操作
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)
# print(curPath)
# print(rootPath)

from web_auto1.common import HTMLTestRunner_cn

# 用例地址
casepath = "D:\\PycharmProjects\\untitled\\web_auto1\\cases"

# 用例读写规则
rule = 'test*.py'

# 查找用例
discover = unittest.defaultTestLoader.discover(start_dir=casepath, pattern=rule)

# html 报告路径
reportPath = os.path.join(curPath, "report\\" + "result.html")
# print(reportPath)
fp =open(reportPath, "wb")

# run
runner = HTMLTestRunner_cn.HTMLTestRunner(stream = fp,
                                          title="测试流程",
                                          description=""
                                          # retry=1  # 失败后重新跑一次
                                          )
runner.run(discover)
fp.close()

# 测试更新代码