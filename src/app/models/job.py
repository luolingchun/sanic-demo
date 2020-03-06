# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 16:41

from tortoise import Model, fields


class Jobs(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50)
    result = fields.CharField(255)

    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now_add=True)

    def __str__(self):
        return f"Job {self.id}: {self.name}"
