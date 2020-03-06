# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 15:46

from sanic_restplus import Api

api = Api(
    version='v1.0',
    title='任务管理 API',
    description='任务管理',
    doc='/swagger',
)

from .job import ns as job_ns

api.add_namespace(job_ns)
