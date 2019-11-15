# Serving ML Models - Some Variations
1. Take a look at *our_model.py* train, and save the model.
(e.g. by running ```python our_model.py ```)
2. Pick one of the implementations below and run it.
3. If you fancy you can load a larger model and use locust
 to run a few performance tests against it.
 
Update: I've ran into FastAPI and added that example because some features
made it my absolute favourite: 
- Async support
- lightning fast & built for ML serving
- OpenAPI Support with one-click documentation & API webinterface to test calls.

### Using batect
This repository uses batect. To run anything here, see how things work, check out 
batect. The only dependency, if you don't want to code anything then is a JVM and 
docker. Then simply run
````bash 
./batect --list-tasks

...
````
and pick what you want to try out.

### Instructions without batect
Here are the things you'll have to do in case you don't want to use batect
or read the batect.yml.

## Run Falcon App
Falcon is the most lightweight solution here, and as such does not bring 
it's own WSGI  (Web Server Gateway Interface). You can use gunicorn 
(the Falcon recommendation) as WSGI and use it as such:

# ```gunicorn falcon_app:app```

Then in browser, or with curl:
1. 
2. 

## Run Flask App
(Uses it's own wsgi server.)

## Run a Nameko App
Nameko is still lightweight, but does come with it's own WSGI, so you can
simply run: 

```nameko run nameko_app```


Then in browser, or with curl:
1.
2. curl -i http://localhost:8000/predict/2/

## Run FastAPI App
FastAPI is lightweight, and lightning fast. It will need a ASGI, which is an even faster 
thing made for Python3.6+. It usually uses uvicron so we're gonna use that too.



## [WIP] Run as Tensorflow Serving
To get our model in tf serving, we need to save it a little bit differently
than we did before (we just pickled it.). So we got to run
```python our_model_to_tf.py``` to convert it.

Then we can: ...

## Load Testing

Run ``` locust -f locustfile.py --host=http://localhost:8000 ```
for Nameko (if you ran it as above). Then you can visit 
http://localhost:8089/ to start the load test and see the results.

## Troubleshooting

Problem " Tensor Tensor(...) is not an element of this graph."
=> That's a problem with threads as they are handled in keras. Don't
forget to use *model._make_predict_function()* as we did here 
(in the load model function.)

Problem "Error: AttributeError: 'local' object has no attribute 'value'"
=> use "threaded=False in app.run()" for flask, or downgrade keras.