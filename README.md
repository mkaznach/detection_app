Welcome to Apple Detection Application!

There are two ways how you can run the app.

1. Using 'uvicorn'

You will need to install all dependencies first.
To see what dependencies you can need check Dockerfile.
After installation run the following command in the project directory:

uvicorn main:app --reload

You will get something like this:

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [28720]
INFO:     Started server process [28722]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

You can open URL in your browser and play with the app.

2. Using Docker container.

Install Docker.
After run the following commands in the project directory:

docker build -t apple_detection .
docker run -d --name mycontainer -p 80:80 apple_detection

Go to http://192.168.99.100/ or http://127.0.0.1/
