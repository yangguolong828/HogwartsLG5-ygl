"""
Basic skeleton of a mitmproxy addon.

Run as follows: mitmproxy -s anatomy.py
"""
from mitmproxy import ctx
from mitmproxy import http

class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        ctx.log.info("Base content %s"% str(flow.id))

    def response(self, flow: mitmproxy.http.HTTPFlow):
       ctx.log.info("response %s"%(str(flow)))

addons = [
    Counter()
]
