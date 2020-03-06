# -*- coding: utf-8 -*-
# @Author  : llc
# @Time    : 2020/3/6 17:21


from tortoise import Model, fields


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(50)

    def __str__(self):
        return f"User {self.id}: {self.name}"