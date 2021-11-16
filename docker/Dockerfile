ENV cur_ref_name=$GITHUB_REF_NAME
FROM python:3.8.12-bullseye

RUN pip install automatic-actions==cur_ref_name

CMD ["date"]
