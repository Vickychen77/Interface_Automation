from db_fixture.mysql_db import DB


datas = {

    # 话题表
    'mz_topic': [
        {'tid': 1, 'topic_name': '魅族E发布会', 'is_recommend': 1, 'link': 'http://www.meizu.com', 'dynamic_num': 0,
         'view_num': 0, 'sort': 0, 'status': 1},
    ],

    # 话题日志表
    'mz_topic_log': [
        {'tlid': 1, 'tid': 1, 'did': 1},
    ],

}

def init_data():
    DB().init_data(datas)

if __name__=='__main__':
    init_data()