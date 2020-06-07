"""
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http


# request不能被改变,写死的
def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.

    if flow.request.pretty_url == "https://www.baidu.com/":
        flow.response = http.HTTPResponse.make(
            200,  # (optional) status code
            b"Hello World!!!!!!",  # (optional) content
            {"Content-Type": "text/html"}  # (optional) headers
        )