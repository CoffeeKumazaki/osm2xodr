FROM python:3.8.0

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apt install -y git
RUN git clone https://github.com/dezhin/osmread.git
RUN cd osmread; python setup.py install; cd ../

# pip
WORKDIR /tmp
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /usr/app

# clearn
RUN rm -rf /var/lib/apt/lists/*