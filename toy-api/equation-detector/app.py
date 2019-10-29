import falcon
import json

app = falcon.API()


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server(
        host='0.0.0.0', port=8080, app=app
    )
    httpd.serve_forever()