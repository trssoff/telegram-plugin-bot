FROM python:3
ADD requirements.txt /root/requirements.txt
RUN pip install -r /root/requirements.txt
