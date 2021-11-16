FROM python:3.8.12-bullseye

RUN export CUR_TAG=$(echo "${GITHUB_REF_NAME:1}") && echo "CUR_TAG: ${CUR_TAG}" && pip install automatic-actions==$CUR_TAG

CMD ["date"]