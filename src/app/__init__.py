# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 15:47


from sanic import Sanic
from sanic_cors import CORS
from sanic_restplus.restplus import restplus
from spf import SanicPluginsFramework
from tortoise.contrib.sanic import register_tortoise

import config


def create_app():
    app = Sanic(__name__)
    app.config.from_object(config)
    # 跨域
    CORS(app)
    # 注册数据库
    register_tortoise(app, db_url=config.DB_URL, modules={"models": ["app.models.job"]},
                      generate_schemas=config.GENERATE_SCHEMAS)

    # 注册api
    from .apis import api
    spf = SanicPluginsFramework(app)
    reg = spf.register_plugin(restplus)
    reg.api(api)

    return app
