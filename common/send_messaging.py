import os
import time
from get_devices import driver


# def send_messaging(content):
#     time.sleep(1)
   driver.find_element_by_id("com.android.mms:id/compose_message_text").send_keys("文本")
   time.sleep(1)
   driver.find_element_by_id("com.android.mms:id/send_message_button").click()
   time.sleep(1)









