# -*- coding:utf-8 -*-
from mailthon import postman, email
p = postman(host='smtp.126.com', port=25, auth=('xxx@126.com', '授权码'))
r = p.send(email(
        # 内容
        content=u'<p>Hello 世界</p>',
        # 标题
        subject='Hello world',
        # 发件人
        sender='John <xxx@126.com>',
        # 收件人列表
        receivers=['xxx@qq.com'],
        # 附件
        attachments=[
        '/xxx/x.pdf,
        '/xxx/x.png'
    ]
    ))
assert r.ok
