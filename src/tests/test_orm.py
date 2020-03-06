# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 17:20

# pylint: disable=E0401,E0611
import logging

from sanic import Sanic, response

from models import User
from tortoise.contrib.sanic import register_tortoise

logging.basicConfig(level=logging.DEBUG)

app = Sanic(__name__)


@app.route("/")
async def list_all(request):
    users = await User.all()
    return response.json({"users": [str(user) for user in users]})


@app.route("/user")
async def add_user(request):
    user = await User.create(name="New User")
    return response.json({"user": str(user)})


register_tortoise(
    app, db_url="sqlite://test.db", modules={"models": ["models"]}, generate_schemas=False
)


if __name__ == "__main__":
    app.run(port=5000)