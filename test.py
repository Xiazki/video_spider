

# data ={
#         "postid": "54131",
#         "title": "专业级粉丝致敬星战",
#         "app_fu_title": "",
#         "wx_small_app_title": "专业级粉丝致敬星战",
#         "intro": "最近上映的《游侠索罗·星球大战外传》口碑扑街，但小编这里却找到一部水准超高的致敬之作。倒不是说特效有多炫酷，但却真真实实地继续了星战精神。该片由Joe sill执导，本站之前推荐过他的另一部科幻作品《EXPO》，同是质量上乘的良心之作。",
#         "count_comment": "19",
#         "pid": "1",
#         "is_album": "0",
#         "post_type": "video",
#         "duration": "451",
#         "is_collect": "0",
#         "content": {
#             "video": [
#                 {
#                     "image": "https://cs.vmovier.com/Uploads/cover/2018-06-01/5b1133fdf0a5f_cut.jpeg",
#                     "title": "专业级粉丝致敬星战《卡拉》",
#                     "duration": "451",
#                     "source_link": "http://oiky1wrat.bkt.clouddn.com/5b113c81e400e.mp4",
#                     "filesize": "260540945",
#                     "resolution": "1920x1080",
#                     "bitrate": "4615132",
#                     "qiniu_url": "https://qiniu-video5.vmoviercdn.com/5b113dee75337.mp4",
#                     "profile_name": "1080P",
#                     "progressive": [
#                         {
#                             "image": "https://cs.vmovier.com/Uploads/cover/2018-06-01/5b1133fdf0a5f_cut.jpeg",
#                             "title": "专业级粉丝致敬星战《卡拉》",
#                             "duration": "451",
#                             "source_link": "http://oiky1wrat.bkt.clouddn.com/5b113c81e400e.mp4",
#                             "filesize": "260540945",
#                             "resolution": "1920x1080",
#                             "bitrate": "4615132",
#                             "qiniu_url": "https://qiniu-video5.vmoviercdn.com/5b113dee75337.mp4",
#                             "profile_name": "1080P"
#                         }
#                     ]
#                 }
#             ]
#         },
#         "image": "https://cs.vmovier.com/Uploads/cover/2018-06-01/5b1133fdf0a5f_cut.jpeg",
#         "rating": "7.9",
#         "publish_time": "1527955560",
#         "count_like": "274",
#         "count_share": "87",
#         "cate": [
#             "科幻"
#         ],
#         "share_link": {
#             "sweibo": "http://h5.vmovier.com/index.html?id=54131&_vfrom=VmovierApp_sweibo",
#             "weixin": "http://h5.vmovier.com/index.html?id=54131&_vfrom=VmovierApp_weixin",
#             "qzone": "http://h5.vmovier.com/index.html?id=54131&_vfrom=VmovierApp_qzone",
#             "qq": "http://h5.vmovier.com/index.html?id=54131&_vfrom=VmovierApp_qq"
#         },
#         "share_title": "专业级粉丝致敬星战 | 场库",
#         "tags": "",
#         "share_sub_title": "爱豆的力量是无穷",
#         "weibo_share_image": "http://service.vmoiver.com/h5/Imagick/vmovier_weibo_share?id=54131",
#         "index_intro": "爱豆的力量是无穷"
#     }
# p = '(%s,%s,%s,%s,%s)'
# title = data['title']
# info = data['intro']
# url = ''
# if len(data['content']['video'][0]['source_link']) > 0:
#     url = data['content']['video'][0]['source_link']
# else:
#     url = data['content']['video'][0]['qiniu_url']
# cover_image = data['content']['video'][0]['image']
# duration = data['duration']
# p = p%(title,info,url,cover_image,str(duration))
# print(p)


print("test")