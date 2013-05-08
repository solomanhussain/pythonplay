import bottle
import os

def application(environ, start_response):
    data = "Hello Soloman you have updated code through CodeEnvy!"
    start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
            ])
    return iter([data])

