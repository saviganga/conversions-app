# select base for dockerfile
FROM python:3.8

#set up environment
ENV PYTHONUNBUFFERED 1

# create a new environment
RUN mkdir /app

# change into the working environment
WORKDIR /app

# create a virtual environment
RUN python -m venv venv

# activate the virtual environment
RUN . venv/bin/activate

#cop files to the working environment
COPY . /app

#install dependencies
RUN pip3 install -r requirements.txt