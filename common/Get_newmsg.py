import time

from get_devices import driver

def get_newmsg(msgtype):
    time.sleep(1)
    #如果传入参数是1，el是最后的控件com.android.mms:id/content_layout；图文，卡券，音频大图等控件
    if msgtype == 1:
        el = driver.find_elements_by_id("com.android.mms:id/content_layout")[-1]
    # 如果传入参数是2，el是最后的控件com.android.mms:id/message_content；纯音频，纯视频，纯图片等控件
    if msgtype == 2:
        el = driver.find_elements_by_id("com.android.mms:id/message_content")[-1]
    # 如果传入参数是3，el是最后的控件com.android.mms:id/ted_common_card_view；卡片控件
    if msgtype == 3:
        el = driver.find_elements_by_id("com.android.mms:id/ted_common_card_view")[-1]
    return el
