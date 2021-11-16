ARG cur_ref_name
FROM python:3.8.12-bullseye

RUN echo ${cur_ref_name}

RUN pip install automatic-actions==${cur_ref_name}

CMD ["date"]
