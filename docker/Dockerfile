FROM python:3.8.12-bullseye

RUN echo $GITHUB_REF_NAME && exit 1

RUN pip install automatic-actions==$GITHUB_REF

CMD ["date"]