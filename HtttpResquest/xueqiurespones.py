from mitmproxy import http


class Counter:
    def __init__(self):
        self.num = 0

    def request(self, flow: http.HTTPFlow) -> None:

        if f"qv5/stock/batch/quote.json" in flow.request.pretty_url:
            with open(r"json文件路径", "r", encoding="utf-8")as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    b"Hello World",  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                )

addons = [
    Counter()
]