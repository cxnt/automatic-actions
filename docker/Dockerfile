FROM python:3.8.12-bullseye

ARG cur_ref_name

RUN pip install automatic-actions==$(echo -n $cur_ref_name | cut -c12-)

CMD ["date"]
