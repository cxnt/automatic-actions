FROM supervisely/base-py-sdk:6.72.85

RUN apt-get update
RUN apt-get install -y zlib1g
RUN apt install -y libssl-dev

RUN cd /tmp \
    && wget https://www.python.org/ftp/python/3.8.13/Python-3.8.13.tgz \
    && tar -xf Python-3.8.13.tgz \
    && cd Python-3.8.13 \
    && ./configure --enable-optimizations \ 
    && make install

RUN rm -f /usr/bin/python* \
    && ln -s /usr/local/bin/python* /usr/bin/ \
    && ln -s /usr/local/bin/python3 /usr/bin/python

RUN python3 --version
RUN python --version
RUN python3.8 --version

RUN pip install attrs
RUN pip install --upgrade pip
RUN pip install requests==2.27.1

RUN pip install supervisely
RUN pip install supervisely[apps]
