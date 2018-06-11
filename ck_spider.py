import threading

from pyspider.libs.base_handler import *
import ck_video


class Handler(BaseHandler):
    crawl_config = {
    }

    p = 1
    size = 10

    cateFlag = {
        '创意': True,
        '励志': True,
        '搞笑': True,
        '运动': True,
        '旅行': True,
        '爱情': True,
        '广告': True,
        '动画': True,
        '剧情': True,
        '音乐': True,
        '科幻': True,
        '记录': True,
        '预告': True,
        '混剪': True,
        '实验': True,
        '生活': True,
        '时尚': True
    }
    pageDict = {
        '创意': 1,
        '励志': 1,
        '搞笑': 1,
        '运动': 1,
        '旅行': 1,
        '爱情': 1,
        '广告': 1,
        '动画': 1,
        '剧情': 1,
        '音乐': 1,
        '科幻': 1,
        '记录': 1,
        '预告': 1,
        '混剪': 1,
        '实验': 1,
        '生活': 1,
        '时尚': 1
    }

    @every(seconds=30)
    def on_start(self):
        for cate in ck_video.cateDirct:
            self.handle_cate(cate)

    @config(age=0)
    def index_page(self, response):
        url = 'https://app.vmovier.com/apiv3/post/view?postid='
        data = response.json['data']
        if any(data):
            for each in response.json['data']:
                self.crawl(url + str(each['postid']), callback=self.detail_page, validate_cert=False)
        else:
            # 重新读取接口数据
            self.pageDict[response.save['cate']] = 1

    @config(priority=2)
    def detail_page(self, response):
        ck_video.handle(response.json['data'])

    def handle_cate(self, cate):
        print("handle------------" + cate)
        # while self.cateFlag[cate]:
        url = 'https://app.vmovier.com/apiv3/post/getPostInCate?p=' + str(self.pageDict[cate]) + '&size=' + str(
            10) + '&cateid=' + str(ck_video.cateDirct[cate])
        self.pageDict[cate] = self.pageDict[cate] + 1
        self.crawl(url, callback=self.index_page, save={'cate': cate}, validate_cert=False)
