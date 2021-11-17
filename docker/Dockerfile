FROM python:3.8.12-bullseye
ARG cur_ref_name

RUN echo $cur_ref_name

COPY VERSION /VERSION
RUN pip install automatic-actions==$(cat /VERSION)

CMD ["date"]
