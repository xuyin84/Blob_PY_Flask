#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import orm
from models import User, Blog, Comment
import  asyncio
#
# async def test(loop):
#
#     await orm.create_pool(loop,user='root', password='123456', db='blog')
#
#     u = User(name='Test', email='test1@example.com', passwd='1234567890', image='about:blank')
#
#     await u.save()
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# # loop.close()

def test():

    yield from orm.create_pool(user='root', password='123456', db='blog')

    u = User(name='Test', email='test1@example.com', passwd='1234567890', image='about:blank')

    yield from u.save()
for x in test():
    pass
# loop = asyncio.get_event_loop()
# loop.run_until_complete(test(loop))
# loop.close()

