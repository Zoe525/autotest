# coding=gbk
#coding:utf-8
import time
import re
from telnetlib import EC

from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import Get_newmsg

from get_devices import driver
def longpress_menu(msgtype,name):
    longpress_menu = []
    time.sleep(1)
    #判断是否有图文，卡券，音频大图等控件
    el = Get_newmsg.get_newmsg(msgtype)
    location = el.get_attribute("bounds")
    x1 = int(location.split("[")[1].split(",")[0])
    y1 = int(location.split(",")[1].split("]")[0])
    x2 = int(location.split("[")[-1].split(",")[0])
    y2 = int(location.split(",")[-1].split("]")[0])
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    #长按消息弹出长按菜单
    driver.tap([(x,y)],1000)
    time.sleep(1)
    #将长按菜单中的内容组成列表，并一次查询哪个是name,是的点击
    el1 = driver.find_elements_by_id("com.android.mms:id/popup_list_window_item_title")
    if name == "多选转发" or name == "多选删除":
        name1 = "多选"
    else:
        name1 = name
    for i in range(len(el1)):
        longpress_menu.append(el1[i].get_attribute("text"))
    if name1 in longpress_menu:
        el1[longpress_menu.index(name1)].click()
        if name == "删除":
            result = delete_msg()
        if name == "分享":
            result = share_msg()
        if name == "收藏":
            result = collection()
        if name == "多选转发":
            result = forward()
        if name == "多选删除":
            result = multi_delete_msg()
        if name == "保存":
            result = get_toast()
        if name == "复制":
            result = get_toast()
    else:
        #如果没有对应菜单，返回"没有该菜单"，点击取消长按菜单
            result = "没有该菜单"
            driver.back()
    print(result)
    return result

def delete_msg():
    time.sleep(1)
    # 如果点击删除则弹出删除确认，点击确认“删除信息”
    driver.find_element_by_id("android:id/button3").click()
    result = "删除成功"
    return result
def multi_delete_msg():
    time.sleep(1)
    # 如果点击删除则弹出删除确认，点击确认“删除信息”
    driver.find_element_by_id("com.android.mms:id/action_select").click()
    time.sleep(1)
    driver.find_element_by_id("com.android.mms:id/action_delete").click()
    time.sleep(1)
    el1 = driver.find_element_by_id("com.android.mms:id/buttonPanel")
    if len(el1.find_elements_by_class_name("android.widget.Button")) == 2:
        driver.find_element_by_id("android:id/button3").click()
    if len(el1.find_elements_by_class_name("android.widget.Button")) == 3:
        driver.find_element_by_id("android:id/button1").click()
    result = "删除成功"
    return result

def share_msg():
    # 长按点击分享后，弹出分享选择应用框
    time.sleep(1)
    el1 = driver.find_element_by_id("oppo:id/oppo_pager")
    el2 = el1.find_elements_by_class_name("android.widget.LinearLayout")
    #在选择会话框选择“短信”应用，通过短信分享
    for i in range(len(el2)):
        if el2[i].find_element_by_id("oppo:id/resolver_item_name").get_attribute("text") == "短信":
            el2[i].click()
            break
    #调用分享转发新建消息函数
    result = new_conversation_share_forward()
    return result

def new_conversation_share_forward():
    time.sleep(1)
    #选择短信分享后，弹出选择会话框，点击“新消息,输入收件人13811631042”
    driver.find_element_by_id("android:id/button1").click()
    time.sleep(1)
    driver.find_element_by_id("com.android.mms:id/recipient_text_view").send_keys("13811631042")
    driver.keyevent(66)
    time.sleep(1)
    if len(driver.find_elements_by_id("com.android.mms:id/recy_attachment_list")) > 0:
        el = driver.find_element_by_id("com.android.mms:id/recy_attachment_list")
        #分别判断在附件栏中是否有视频，文本，名片，语音，图片，位置有返回result=分享转发xxx
        if len(el.find_elements_by_id("com.android.mms:id/message_video_thumbnail_image")) > 0:
            result = "分享转发视频"
        elif len(el.find_elements_by_id("com.android.mms:id/message_audio_thumbnail_image")) > 0:
            result = "分享转发音频"
        elif len(el.find_elements_by_id("com.android.mms:id/contact_icon")) > 0:
            result = "分享转发名片"
        elif len(el.find_elements_by_id("com.android.mms:id/attachment_image_view")) > 0:
            result = "分享转发图片/位置"
    else:
        #附件栏里没有视频，音频，图片，名片，位置，判断是否有文本，如果文案是默认的网络信息/短信，则分享转发失败，否则返回result=分享转发文本原文
        text =  driver.find_element_by_id("com.android.mms:id/compose_message_text").get_attribute("text")
        if text != "网络信息" and text != "短信":
            result = text
        else:
            result = "分享转发失败"
    driver.find_element_by_id("com.android.mms:id/action_cancel").click()
    return result
def collection():
    #判断收藏icon是否存在，存在返回result = "收藏成功"，没有返回result = "收藏失败"
    if len(driver.find_elements_by_id("com.android.mms:id/locked_indicator")) > 0:
        result = "收藏成功"
    else:
        result = "收藏失败"
    return result
def forward():
    time.sleep(1)
    #点击转发
    el = driver.find_element_by_id("com.android.mms:id/action_forward")
    if el.is_enabled() == True:
        driver.find_element_by_id("com.android.mms:id/action_forward").click()
        time.sleep(1)
        # 调用分享转发新建消息函数
        result = new_conversation_share_forward()
        time.sleep(1)
    else:
        result = "不可转发"
    driver.back()
    return  result

def get_toast(driver=driver,text=None, timeout=5, poll_frequency=0.1):
    #获取Tost的内容
    if text:
        toast_loc = ("//*[contains(@text, '%s')]" %text)
    else:
        toast_loc = "//*[@class='android.widget.Toast']"
    try:
       WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(('xpath', toast_loc)))
       toast_elm = driver.find_element_by_xpath(toast_loc)
       if toast_elm.text.find("附件已保存至") != -1:
       #将toast提示截取，截掉小时和秒（因代码会有延迟，所以前后会差几秒，除去小时和秒，避免误差）
            result = re.search(r'.*?\d{8}_', toast_elm.text).group(0) + re.search(r'01.*', toast_elm.text).group(0)
       else:
           result = toast_elm.text
    except:
        result = ""
    return result
    print(result)

# longpress_menu("保存")
# longpress_menu("分享")
# longpress_menu("多选转发")
# longpress_menu("收藏")
# longpress_menu("删除")
