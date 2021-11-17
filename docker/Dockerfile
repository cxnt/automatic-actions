FROM python:3.8.12-bullseye

COPY VERSION /VERSION
RUN pip install automatic-actions==$(cat /VERSION)

CMD ["date"]
