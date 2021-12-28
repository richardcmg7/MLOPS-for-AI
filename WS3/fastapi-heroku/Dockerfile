FROM python:3.8

WORKDIR /flask-app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY ./app /flask-app


ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]