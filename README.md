# gifunny-backend

The backend of GIFunny has been developed using Flask, a Python framework.
It consists in a software layer between the frontend and the GIF provider service.

## Architecture

This software consists of two modules:

- model: it contains the classes needed to handle the gif data structure.
- persistence: it contains the classes to handle the interaction between this layer and the GIF provider systems.

In app.py there is the structure to handle the incoming HTTP requests.

### Model

The class Gif extends ABC (AbstractBaseClass) to ease the assignment of the fields.
Moreover, it provides methods:

- to create an instance starting from a dictionary.
- to create a dictionary starting from the state of the object.

This is very useful to create the responses.

### Persistence

In this module there is a class that takes care of the interaction with GIPHY provider. An instance of GiphyManager:

1. takes the request parameters
2. builds the request
3. handle the response: 
    
    - it raises an ad-hoc exception if an error happens.This exception encapsulates the possible exception that can happen.
    - it builds the list of gifts if the request is successful.

## Endpoints

### GIFS

- GET

| name      |  type     | data type               | description                                                           |
|-----------|-----------|-------------------------|-----------------------------------------------------------------------|
| query      |  required | string   | The query to   |
| limit      |  required | integer  | Limit the number of the results to a certain number  |

## How to use

### With Docker

1. Build the Dockerfile
2. Run the docker image with the following settings:
    - host port: 5000
    - add an environment variable GIPHY_TOKEN=<*YOUR-TOKEN*>
3. Go to http://127.0.0.1:5000/, you should get the following text: 'Welcome in GIFunny backend'.

### Without Docker

1. Install Python 3 locally
2. Go in the project root directory
3. Run <code>pip3 install -r requirements.txt</code>
4. Run <code>pyhton -m flask run --host=0.0.0.0 --port=5000</code>