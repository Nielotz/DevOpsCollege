FROM python

RUN python3.11 -m pip install pip --upgrade

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get autoremove -y && \
    apt-get clean

RUN git clone https://github.com/Nielotz/DevOpsCollege.git app

RUN python3.11 -m pip install -r app/api/requirements.txt

CMD python3.11 app/main.py