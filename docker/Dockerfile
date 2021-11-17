FROM python:3.8.12-bullseye

ARG tag_ref_name

RUN pip install automatic-actions==$(echo -n $tag_ref_name | cut -c2-)

CMD ["date"]
