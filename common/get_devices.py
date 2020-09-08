import time
from appium import webdriver
#testadfasdfASDFASDFASDFADFASDF
des={
    'platformName': 'Android',
    'platformVersion': '10', #填写android的系统版本
    'deviceName': 'oppo reno', #填写设备名称
    'appPackage': 'com.android.mms', #填写被测试包名
    'appActivity': '.ui.ConversationList', #填写被测试app入口
    'udid': '88ccb924', # 填写通过命令行 adb devices 查看到的 uuid
    'noReset': True,
    'unicodeKeyboard': True,
    'resetKeyboard': True,
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', des)

# driver.find_element_by_xpath('//android.widget.TextView[@text="消息"]').click()
# time.sleep(1)
driver.find_element_by_id('com.android.mms:id/action_start_new_conversation').click()
time.sleep(1)
driver.find_element_by_id('com.android.mms:id/recipient_text_view').send_keys('13811346164')
driver.keyevent(66)
time.sleep(1)


