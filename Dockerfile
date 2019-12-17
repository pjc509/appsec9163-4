FROM ubuntu:16.04

MAINTAINER Pete Crefeld "pjc509@nyu.edu"

RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev 

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app
ENV LANG=C.UTF-8
ENV PYTHONIOENCODING=utf-8
#ENTRYPOINT [ "python" ]

#CMD [ "app.py" ]
CMD ["flask", "run", "--host=0.0.0.0"]
#ADD exporter.py /exporter.py
#ADD boot.sh /boot.sh
#CMD ["/app/", "boot.sh"]
#CMD ["boot.sh"]
