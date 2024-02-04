# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx
RUN apt-get update \
    && apt-get install -y libglib2.0-0
RUN pip install --upgrade pip
RUN pip install torch==2.0
RUN pip install fastapi
RUN pip install uvicorn
RUN pip install -U openmim
RUN pip install python-multipart
RUN mim install mmengine
RUN mim install "mmcv>=2.0.0"
RUN mim install mmdet

# Download the mmdetection model files (config and checkpoint) and place them in the /app directory

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
