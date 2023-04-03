FROM python

RUN python3.11 -m pip install pip --upgrade

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git && \
    apt-get autoremove -y && \
    apt-get clean

RUN git clone https://github.com/Nielotz/DevOpsCollege.git app

RUN python3.11 -m pip install -r app/api/requirements.txt

CMD cd app && \
    git switch test && \
    python3.11 main.py