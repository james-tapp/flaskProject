FROM python:3.6
WORKDIR /home/alexandertapp/docker/flaskProject
ENV FLASK_ENV production
ENV FLASK_APP run.py
COPY requirements .
RUN pip3 install -r requirements
COPY . .
ENTRYPOINT ["/usr/local/bin/flask", "run", "--host=0.0.0.0"]

