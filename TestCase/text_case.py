import time
import unittest
import get_devices
import Longpress_menu
import Collection


class TextTest(unittest.TestCase):
    def test_text01(self):
        if len(self.driver.find_elements_by_id("com.android.mms:id/message_text")) > 0:
            el = self.driver.find_elements_by_id("com.android.mms:id/message_text")[-1]
            result= '文本接收正常'
        else:
            result='没有接收'
        self.assertEqual(result,'文本接收正常')
    def test_text02(self):
        # 长按菜单->复制，确认是否有toast提示“文本已复制”
        copy = Longpress_menu.longpress_menu(3, "复制")
        self.assertEqual(copy, "文本已复制")
    def test_text03(self):
        # 分享，确认分享的内容是否是文本本身
        share = Longpress_menu.longpress_menu(3, "分享")
        self.assertEqual(share, "c2c文本测试")
    def test_text04(self):
        # 转发，确认转发的内容是否是文本本身
        forward = Longpress_menu.longpress_menu(3, "多选转发")
        self.assertEqual(forward, "c2c文本测试")
    def test_text05(self):
        # 点击长按菜单收藏，查看收藏图标是否存在，存在collection == 收藏成功，没有collection ==收藏失败
        collection = Longpress_menu.longpress_menu(3, "收藏")
        self.assertEqual(collection, "收藏成功")
        self.driver.back()
    def test_text06(self):
        # 进入收藏列表获取收藏文案，点击收藏内容进入会话
        title = Collection.entry_collection()
        self.assertEqual(title, "c2c文本测试")
        time.sleep(1)
    def test_text07(self):
        # 删除消息
        Longpress_menu.longpress_menu(3, "删除")
        time.sleep(1)
        self.driver.back()