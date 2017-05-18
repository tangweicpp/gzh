#!/usr/bin/env python
#coding:utf-8
import hashlib
import web
import receive
import reply
from media import get_mediaId

class Handle(object):
    def GET(self):
        try:
            data = web.input()
            if len(data) == 0:
                return 'hello, this is handle view'
            signature = data.signature
            timestamp = data.timestamp
            nonce = data.nonce
            echostr = data.echostr
            token = 'tangweicpp'

            list = [token, timestamp, nonce]
            list.sort()
            sha1 = hashlib.sha1()
            map(sha1.update, list)
            hashcode = sha1.hexdigest()
            print 'handle/GET func: hashcode, signature: ', hashcode, signature
            if hashcode == signature:
                return echostr
            else:
                return ''
        except Exception, Arg:
            return Arg

    def POST(self):
        try:
            webData = web.data()
            print 'Handle Post webdata is ', webData
            recMsg = receive.parse_xml(webData)
            if isinstance(recMsg, receive.Msg):
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName
                if recMsg.MsgType == 'text':
                    content = recMsg.Content
                    replyMsg = reply.TextMsg(toUser, fromUser, content)
                if recMsg.MsgType == 'image':
                    mediaId = get_mediaId()
                    print '2:mediaId = ', mediaId
                    replyMsg = reply.ImageMsg(toUser, fromUser, mediaId)
                
                return replyMsg.send()
            if isinstance(recMsg, receive.EventMsg):
                if recMsg.Event == 'CLICK':
                    if recMsg.EventKey == 'mpGuide':
                        content = u'编写中,尚未完成'.encode('utf-8')
                        replyMsg = reply.TextMsg(toUser, fromUser, content)
                        return replyMsg.send()
            print '暂且不处理'
            return reply.Msg().send()
        except Exception, Arg:
            return Arg
