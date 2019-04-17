import json
from nameko.web.handlers import http
import our_model

class HttpService:
    name = "nameko_http"

    def __init__(self):
        self.model = our_model.load_trained_model()

    @http('GET', '/predict/<int:value>/')
    def get_method(self, request, value):
        pred = self.model.predict([value])
        return json.dumps({"payload":f"the prediction for {pred} is: {pred}"})


    @http('POST', '/post')
    def do_post(self, request):
        return u"received: {}".format(request.get_data(as_text=True))
