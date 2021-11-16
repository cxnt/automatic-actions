FROM python:3.8.12-bullseye

RUN sleep 30 && pip install automatic-actions==$GITHUB_REF_NAME

CMD ["date"]