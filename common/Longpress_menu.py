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
    #�ж��Ƿ���ͼ�ģ���ȯ����Ƶ��ͼ�ȿؼ�
    el = Get_newmsg.get_newmsg(msgtype)
    location = el.get_attribute("bounds")
    x1 = int(location.split("[")[1].split(",")[0])
    y1 = int(location.split(",")[1].split("]")[0])
    x2 = int(location.split("[")[-1].split(",")[0])
    y2 = int(location.split(",")[-1].split("]")[0])
    x = (x1 + x2) // 2
    y = (y1 + y2) // 2
    #������Ϣ���������˵�
    driver.tap([(x,y)],1000)
    time.sleep(1)
    #�������˵��е���������б���һ�β�ѯ�ĸ���name,�ǵĵ��
    el1 = driver.find_elements_by_id("com.android.mms:id/popup_list_window_item_title")
    if name == "��ѡת��" or name == "��ѡɾ��":
        name1 = "��ѡ"
    else:
        name1 = name
    for i in range(len(el1)):
        longpress_menu.append(el1[i].get_attribute("text"))
    if name1 in longpress_menu:
        el1[longpress_menu.index(name1)].click()
        if name == "ɾ��":
            result = delete_msg()
        if name == "����":
            result = share_msg()
        if name == "�ղ�":
            result = collection()
        if name == "��ѡת��":
            result = forward()
        if name == "��ѡɾ��":
            result = multi_delete_msg()
        if name == "����":
            result = get_toast()
        if name == "����":
            result = get_toast()
    else:
        #���û�ж�Ӧ�˵�������"û�иò˵�"�����ȡ�������˵�
            result = "û�иò˵�"
            driver.back()
    print(result)
    return result

def delete_msg():
    time.sleep(1)
    # ������ɾ���򵯳�ɾ��ȷ�ϣ����ȷ�ϡ�ɾ����Ϣ��
    driver.find_element_by_id("android:id/button3").click()
    result = "ɾ���ɹ�"
    return result
def multi_delete_msg():
    time.sleep(1)
    # ������ɾ���򵯳�ɾ��ȷ�ϣ����ȷ�ϡ�ɾ����Ϣ��
    driver.find_element_by_id("com.android.mms:id/action_select").click()
    time.sleep(1)
    driver.find_element_by_id("com.android.mms:id/action_delete").click()
    time.sleep(1)
    el1 = driver.find_element_by_id("com.android.mms:id/buttonPanel")
    if len(el1.find_elements_by_class_name("android.widget.Button")) == 2:
        driver.find_element_by_id("android:id/button3").click()
    if len(el1.find_elements_by_class_name("android.widget.Button")) == 3:
        driver.find_element_by_id("android:id/button1").click()
    result = "ɾ���ɹ�"
    return result

def share_msg():
    # �����������󣬵�������ѡ��Ӧ�ÿ�
    time.sleep(1)
    el1 = driver.find_element_by_id("oppo:id/oppo_pager")
    el2 = el1.find_elements_by_class_name("android.widget.LinearLayout")
    #��ѡ��Ự��ѡ�񡰶��š�Ӧ�ã�ͨ�����ŷ���
    for i in range(len(el2)):
        if el2[i].find_element_by_id("oppo:id/resolver_item_name").get_attribute("text") == "����":
            el2[i].click()
            break
    #���÷���ת���½���Ϣ����
    result = new_conversation_share_forward()
    return result

def new_conversation_share_forward():
    time.sleep(1)
    #ѡ����ŷ���󣬵���ѡ��Ự�򣬵��������Ϣ,�����ռ���13811631042��
    driver.find_element_by_id("android:id/button1").click()
    time.sleep(1)
    driver.find_element_by_id("com.android.mms:id/recipient_text_view").send_keys("13811631042")
    driver.keyevent(66)
    time.sleep(1)
    if len(driver.find_elements_by_id("com.android.mms:id/recy_attachment_list")) > 0:
        el = driver.find_element_by_id("com.android.mms:id/recy_attachment_list")
        #�ֱ��ж��ڸ��������Ƿ�����Ƶ���ı�����Ƭ��������ͼƬ��λ���з���result=����ת��xxx
        if len(el.find_elements_by_id("com.android.mms:id/message_video_thumbnail_image")) > 0:
            result = "����ת����Ƶ"
        elif len(el.find_elements_by_id("com.android.mms:id/message_audio_thumbnail_image")) > 0:
            result = "����ת����Ƶ"
        elif len(el.find_elements_by_id("com.android.mms:id/contact_icon")) > 0:
            result = "����ת����Ƭ"
        elif len(el.find_elements_by_id("com.android.mms:id/attachment_image_view")) > 0:
            result = "����ת��ͼƬ/λ��"
    else:
        #��������û����Ƶ����Ƶ��ͼƬ����Ƭ��λ�ã��ж��Ƿ����ı�������İ���Ĭ�ϵ�������Ϣ/���ţ������ת��ʧ�ܣ����򷵻�result=����ת���ı�ԭ��
        text =  driver.find_element_by_id("com.android.mms:id/compose_message_text").get_attribute("text")
        if text != "������Ϣ" and text != "����":
            result = text
        else:
            result = "����ת��ʧ��"
    driver.find_element_by_id("com.android.mms:id/action_cancel").click()
    return result
def collection():
    #�ж��ղ�icon�Ƿ���ڣ����ڷ���result = "�ղسɹ�"��û�з���result = "�ղ�ʧ��"
    if len(driver.find_elements_by_id("com.android.mms:id/locked_indicator")) > 0:
        result = "�ղسɹ�"
    else:
        result = "�ղ�ʧ��"
    return result
def forward():
    time.sleep(1)
    #���ת��
    el = driver.find_element_by_id("com.android.mms:id/action_forward")
    if el.is_enabled() == True:
        driver.find_element_by_id("com.android.mms:id/action_forward").click()
        time.sleep(1)
        # ���÷���ת���½���Ϣ����
        result = new_conversation_share_forward()
        time.sleep(1)
    else:
        result = "����ת��"
    driver.back()
    return  result

def get_toast(driver=driver,text=None, timeout=5, poll_frequency=0.1):
    #��ȡTost������
    if text:
        toast_loc = ("//*[contains(@text, '%s')]" %text)
    else:
        toast_loc = "//*[@class='android.widget.Toast']"
    try:
       WebDriverWait(driver, timeout, poll_frequency).until(EC.presence_of_element_located(('xpath', toast_loc)))
       toast_elm = driver.find_element_by_xpath(toast_loc)
       if toast_elm.text.find("�����ѱ�����") != -1:
       #��toast��ʾ��ȡ���ص�Сʱ���루���������ӳ٣�����ǰ����룬��ȥСʱ���룬������
            result = re.search(r'.*?\d{8}_', toast_elm.text).group(0) + re.search(r'01.*', toast_elm.text).group(0)
       else:
           result = toast_elm.text
    except:
        result = ""
    return result
    print(result)

# longpress_menu("����")
# longpress_menu("����")
# longpress_menu("��ѡת��")
# longpress_menu("�ղ�")
# longpress_menu("ɾ��")
