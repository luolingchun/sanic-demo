# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 15:53


from sanic_restplus import Namespace, reqparse, Resource

from app.models.job import Jobs

from code import Code

ns = Namespace('v1/job', description='任务管理 API接口')

job_list_param = reqparse.RequestParser()
job_list_param.add_argument(name='name', type=str, location='form', required=True, help="任务名称")


@ns.route('')
class JobListAPI(Resource):
    @ns.doc(id='get job list', description='获取任务列表')
    async def get(self, request):
        """获取任务列表"""
        # jobs = await Jobs.all()
        # return {'code': Code.Success, 'data': [{
        #     "id": job.id,
        #     "name": job.name,
        #     "result": job.result,
        #     "create_at": str(job.created_at),
        #     "update_at": str(job.updated_at),
        # } for job in jobs]}
        data="""
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
        return data

    @ns.doc(id='post job', description='添加任务')
    @ns.expect(job_list_param)
    async def post(self, request):
        """添加任务"""
        form = request.form
        name = form.get('name')
        job = await Jobs.create(name=name, result="")
        return {'code': 0, 'data': {
            "id": job.id,
            "name": job.name,
            "result": job.result,
            "create_at": str(job.created_at),
            "update_at": str(job.updated_at),
        }}


job_param = reqparse.RequestParser(bundle_errors=True)
job_param.add_argument(name='job_id', type=str, location='path', required=True, help='任务id')


@ns.route('/<id>')
@ns.param('id', '任务id', 'path', required=True, type=str)
class JobAPI(Resource):
    @ns.doc(id='get job', description='获取单个任务详情')
    async def get(self):
        """获取单个任务"""
        return {'code': 0, 'data': []}

    @ns.doc(id='requeue job', description='重新开始任务')
    async def put(self, job_id):
        """重新开始任务"""

        return {'code': 0, 'data': 'job_id'}

    @ns.doc(id='delete job', description='删除任务')
    async def delete(self, job_id):
        """删除任务"""
        return {'code': 0, 'data': 'job_id'}
