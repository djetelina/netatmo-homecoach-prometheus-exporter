FROM python:3.8-alpine3.10

RUN pip install prometheus_client requests

EXPOSE 5000

COPY main.py /homecoach_exporter.py

ENTRYPOINT ["python", "/homecoach_exporter.py"]
