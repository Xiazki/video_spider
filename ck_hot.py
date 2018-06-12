from pyspider.libs.base_handler import *

import ck_video


class HotHandler(BaseHandler):
    crawl_config = {
    }

    p = 1

    @every(seconds=2)
    def on_start(self):
        self.crawl('https://app.vmovier.com/apiv3/post/getPostByTab?p=' + str(self.p) + "&size=10&tab=hot",
                   callback=self.index_page)
        self.p = self.p + 1

    @config(age=0)
    def index_page(self, response):
        url = 'https://app.vmovier.com/apiv3/post/view?postid='
        data = response.json['data']
        if any(data):
            for each in response.json['data']:
                self.crawl(url + str(each['postid']), callback=self.detail_page, validate_cert=False)
        else:
            # 重新读取接口数据
            self.p = 1

    @config(priority=2)
    def detail_page(self, response):
        ck_video.handle(response.json['data'])
