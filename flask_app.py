import flask
import our_model

app = flask.Flask(__name__)
model = None

@app.route("predict/{some_param}/", methods=["GET"])
def predict(some_param):
    pass


if __name__ == "__main__":
    print(("* Loading Keras model and Flask starting server..."
        "please wait until server has fully started"))
    our_model.load_trained_model()
    app.run(threaded=False)