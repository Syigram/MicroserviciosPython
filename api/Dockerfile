FROM python:3.7-slim-buster

# Port to expose
EXPOSE 5000

# PROJECTHOME Variable
ARG PROJECTHOME=/home/prodigious/form_app

# Create project dir and update WORKDIR
RUN mkdir -p $PROJECTHOME
WORKDIR $PROJECTHOME

# Copy dependencies file
COPY requirements.txt .

# Install dependencies
RUN pip install -r requirements.txt

# Copy the rest of the files
COPY db_form.sqlite3 .
COPY main.py .

CMD ["python", "main.py"]
