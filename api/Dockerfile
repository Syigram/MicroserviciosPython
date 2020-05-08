FROM python:3.7-slim-buster

# Port to expose
EXPOSE 5000

#Add Flask ENV variable
ENV FLASK_ENV development

# PROJECTHOME Variable
ARG PROJECTHOME=/home/prodigious/api

# Create project dir and update WORKDIR
RUN mkdir -p $PROJECTHOME
WORKDIR $PROJECTHOME

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy files
COPY main.py .

# Copy directories
COPY app app
COPY config config
COPY models models

CMD ["flask", "run", "--host=0.0.0.0"]
