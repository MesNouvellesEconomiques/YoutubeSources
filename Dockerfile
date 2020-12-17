FROM python

COPY ./code /code
COPY ./sources.json /data/sources.json

CMD ["bash"]