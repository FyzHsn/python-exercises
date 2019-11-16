import falcon
import json


class EquationDetectionRequestHandler:
    def on_get(self, req, resp):
        json_output = json.dumps(
            {'equation_in_text': False}
        )

        resp.content_type = 'application/json'
        resp.body = json_output
        resp.status = falcon.HTTP_201
