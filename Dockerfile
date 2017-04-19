FROM python:3.5.3
MAINTAINER furion <_@furion.me>

COPY . /src
WORKDIR /src

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "webapi.py"]
