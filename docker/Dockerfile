ARG GITHUB_REF_NAME
FROM python:3.8.12-bullseye

RUN echo GITHUB_REF_NAME
RUN echo ${GITHUB_REF_NAME}

RUN pip install automatic-actions==${GITHUB_REF_NAME}

CMD ["date"]