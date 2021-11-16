FROM python:3.8.12-bullseye

RUN version=`cat VERSION`
RUN echo "version: $version"


RUN pip install automatic-actions==$version

CMD ["date"]
