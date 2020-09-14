import time

import re

from get_devices import driver



def entry_collection():
    time.sleep(1)
    #点击右上角菜单按钮
    driver.find_element_by_id("com.android.mms:id/action_more").click()
    #将菜单中的内容组成列表，并一次查询哪个是我的收藏，查询到后点击我的收藏进入收藏列表
    time.sleep(2)
    el = driver.find_element_by_id("com.android.mms:id/color_popup_list_view")
    el1 = el.find_elements_by_id("com.android.mms:id/popup_list_window_item_title")
    for i in range(len(el1)):
        if el1[i].get_attribute("text") == "我的收藏":
            el1[i].click()
            break
    #获取收藏列表第一个收藏的控件，获取对应的文案
    time.sleep(2)
    # el2 = driver.find_element_by_id("android:id/list")
    # el3 = el2.find_elements_by_class_name("android.widget.RelativeLayout")
    el2 = driver.find_elements_by_id("com.android.mms:id/message_text")
    collection_title = el2[0].get_attribute("text")
    collection_title_list = "[服务号消息][语音][位置][名片][图片][视频]"
    #截取文案前面的[]内容，如果没有[]，则是纯文本，返回文本内容
    try:
        collection_title1 = re.search(r'^\[.+?\]',collection_title).group()
        #如果文案里有[]但是不在collection_title_list，则是纯文本，返回文本内容
        if collection_title_list.find(collection_title1) != -1:
            collection_title = collection_title1
        else:
            print("纯文本")
    except:
        print("纯文本")
    print(collection_title)
        #点击第一个收藏进入会话
    el2[0].click()
    return collection_title


# collection()
# entry_collection()