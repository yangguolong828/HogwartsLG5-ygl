
import mitmproxy.http
from mitmproxy import ctx
from mitmproxy import http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow:mitmproxy.http.HTTPFlow):
        self.num = self.num + 1
        ctx.log.info("We've seen %d flows" % self.num)
        ctx.log.info("Base content %s"% str(flow.id))

    def response(self, flow: mitmproxy.http.HTTPFlow):
        ctx.log.info("response %s"%(str(flow)))

    def request(self, flow: http.HTTPFlow) -> None:

        if "baidu" in flow.request.pretty_url:
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                b"Hello World",  # (optional) content
                {"Content-Type": "text/html"}  # (optional) headers
            )

addons = [
    Counter()
]
