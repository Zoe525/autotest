import os
import time
from get_devices import driver


def send_messaging(phone,text):
   # 点击新建信息
   driver.find_element_by_id('com.android.mms:id/action_start_new_conversation').click()
   time.sleep(1)
   # 输入电话号码
   driver.find_element_by_id('com.android.mms:id/recipient_text_view').send_keys(phone)
   driver.keyevent(66)
   time.sleep(1)
   # 输入文本发送
   driver.find_element_by_id('com.android.mms:id/compose_message_text').send_keys(text)
   time.sleep(1)
   driver.find_element_by_id('com.android.mms:id/send_message_button').click()
   time.sleep(3)
  # 判断最后一条消息的内容长度>0就是有最后一条消息，否则消息没有发送出去
   if len(driver.find_elements_by_id("com.android.mms:id/message_text")) > 0:
      el = driver.find_elements_by_id("com.android.mms:id/message_text")[-1]
      msg_content = el.find_element_by_id("com.android.mms:id/message_text").get_attribute("text")
   else:
      msg_content = "没有发送出去"
   # 判断是否是最后一条发送的消息
   if len(driver.find_elements_by_id("com.android.mms:id/message_status")) > 0:
      el = driver.find_elements_by_id("com.android.mms:id/message_status")[-1]
      msg_status = el.find_element_by_id("com.android.mms:id/message_status").get_attribute("text")
   else:
      msg_status = "没有获取发送状态"
   return msg_status,msg_content




# send_messaging('13811346164','dada大文本')







