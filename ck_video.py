from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()
engine = create_engine("mysql+pymysql://root:xiaxiang@localhost:3306/test?charset=utf8", encoding="utf-8", echo=True)
Session = sessionmaker(bind=engine)

cateDirct = {
    '创意': 6,
    '励志': 7,
    '搞笑': 8,
    '运动': 10,
    '旅行': 11,
    '爱情': 12,
    '广告': 13,
    '动画': 16,
    '剧情': 17,
    '音乐': 18,
    '科幻': 23,
    '记录': 24,
    '预告': 43,
    '混剪': 44,
    '实验': 45,
    '生活': 78,
    '时尚': 88
}


class CkVideo(Base):
    __tablename__ = 'ck_video'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    info = Column(String)
    url = Column(String)
    cateId = Column('cate_id', Integer)
    cate = Column(String)
    coverImage = Column('cover_image', String)
    duration = Column(BigInteger)


def handle(data):
    ckVideo = CkVideo()
    ckVideo.title = data['title']
    ckVideo.info = data['intro']
    ckVideo.url = data['content']['video'][0]['qiniu_url']
    ckVideo.coverImage = data['content']['video'][0]['image']
    ckVideo.duration = data['duration']
    ckVideo.cate = '其他'
    ckVideo.cateId = 0
    if 'cate'in data:
        cate = data['cate'][0]
        if cate in cateDirct:
            ckVideo.cate = cate
            ckVideo.cateId = cateDirct[cate]
    session = Session()
    if ckVideo.url.split() == '':
        return
    list = session.query(CkVideo).filter(CkVideo.url == ckVideo.url).all()
    if any(list):
        return
    session.add(ckVideo)
    session.commit()
