# coding=utf-8
import unittest
import os, sys, json, time

# from .mac.mac_requests import MACRequests

# parentdir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, parentdir)
from db_fixture import test_data
from interface.mac.mac_requests import MACRequests

from db_fixture.mysql_db import DB
import random
from nose_parameterized import parameterized


def setUpModule():
    test_data.init_data()  # 初始化测试数据


class GetRecommendTopicListTest(unittest.TestCase):
    """ 获取推荐话题 """

    def setUp(self):
        self.url = "/topic/get_recommend_topic_list"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("num_small_1", -1, 10021, '参数不正确'),
        ("num_big_101", 101, 12201, '获取话题数量不能大于100'),
        ("get_success", 1, 200, '获取成功'),
    ])
    def test_get_list(self, name, num, status, message):
        """ 获取问卷列表 """
        self.result = MACRequests().get(self.url, {'num': num})
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        if status == 200:
            self.assertEqual(self.result['data']['list'][0]['topic_name'], '魅族E发布会')


class GetDynamicListTest(unittest.TestCase):
    """ 获取话题的动态列表 """

    def setUp(self):
        self.url = "/topic/get_dynamic_list"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("tid_small_1", -1, 10021, '参数不正确'),
        ("tid_error", 901, 12202, '话题不存在'),
        ("get_success", 1, 200, '获取成功'),
    ])
    def test_get_dynamic_list(self, name, tid, status, message):
        """ 获取问卷列表 """
        self.result = MACRequests().get(self.url, {'tid': tid})
        self.assertEqual(self.result['status'], status)
        self.assertEqual(self.result['message'], message)
        if status == 200:
            self.assertEqual(self.result['data']['count'], '1')


class TopicSaveTest(unittest.TestCase):
    """ 保存话题数据 """

    def setUp(self):
        self.url = "/topic/topic_save"

    def tearDown(self):
        print(self.result)

    @parameterized.expand([
        ("all_null", '', '', 10021, ''),
        ("all_null", '', '奥运会', 10021, ''),
    ])
    def test_get_dynamic_list(self, name, did, topic_name, status, message):
        """ 获取问卷列表 """
        self.result = MACRequests().get(self.url, {'tid': did, 'topic_name': topic_name})
        self.assertEqual(self.result['status'], status)
        if did == topic_name == '':
            self.assertIn('话题名称 不允许为空', self.result['message'])
            self.assertIn('动态ID 不允许为空', self.result['message'])
        if did == '' and topic_name != '':
            self.assertIn('动态ID 不允许为空', self.result['message'])
        if status == 200:
            self.assertEqual(self.result['data']['count'], '1')


if __name__ == "__main__":
    unittest.main()
