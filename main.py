#!/usr/bin/env python

import web
from handle import Handle

urls = ('/weixin', 'Handle')
'''
class Handle(object):
    def GET(self):
        return 'Hello, this a test'
'''
if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
