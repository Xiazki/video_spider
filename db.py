import pymysql


def ck_insert_video(data):
    sql = 'INSERT into ck_video(title,info,url,cover_image,duration) VALUES(%s,%s,%s,%s,%s)'
    title = data['title']
    info = data['intro']
    url = ''
    if len(data['content']['video'][0]['source_link']) > 0:
        url = data['content']['video'][0]['source_link']
    else:
        url = data['content']['video'][0]['qiniu_url']
    cover_image = data['content']['video'][0]['image']
    duration = data['duration']
    # p = p%(title, info, url, cover_image, str(duration))
    conn = pymysql.connect(host="127.0.0.1", user='root', passwd='xiaxiang', db='test',charset = 'utf8')
    cur = conn.cursor()
    cur.execute(sql, (title, info, url, cover_image, str(duration)))
    conn.commit()
    cur.close()
    conn.close()
