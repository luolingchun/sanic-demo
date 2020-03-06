# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 18:09


from sanic import Sanic
from sanic import response

app = Sanic(__name__)


@app.route('/v1/job')
async def get(request):
    data = """
    7 {
    "code": 0,
    "data": [
        {
            "id": 1,
            "name": "\u662f\u5426\u63d0\u4f9b",
            "result": "",
            "create_at": "2020-03-06 09:46:04.708042",
            "update_at": "2020-03-06 09:46:04.709040"
        },
        {
            "id": 2,
            "name": "\u6211\u662f\u6cd5\u5e08",
            "result": "",
            "create_at": "2020-03-06 09:51:19.888863",
            "update_at": "2020-03-06 09:51:19.888863"
        }
    ]
}"""
    return response.text(str(data))


if __name__ == '__main__':
    app.run()
