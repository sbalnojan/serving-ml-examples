import falcon
import our_model

class ModelServer(object):
    def __init__(self, model):
        self.__model = model
    def on_get(self, req, resp, some_param):
        """Handles GET requests. Retrieve some old result. """
        resp.status = falcon.HTTP_200  # This is the default status
        some_param=int(some_param)
        pred = model.predict([some_param])
        resp.body = f"the prediction for {some_param} is: {pred}"


model = our_model.load_trained_model()

app = falcon.API()
app.add_route('/predict/{some_param}/', ModelServer(model))

class ModelServer(object):
    def __init__(self, model):
        self.__model = model
    def on_get(self, req, resp, some_param):
        """Handles GET requests. Retrieve some old result. """
        resp.status = falcon.HTTP_200  # This is the default status
        resp.body = ("this is it: " + str(some_param))

    def on_post(self, req, resp):
        """Handles POST requests.  Pass some model input... """
        pass

app_2 = falcon.API()
