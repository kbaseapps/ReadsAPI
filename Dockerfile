FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

RUN pip install --upgrade pip
RUN apt-get update
RUN apt-get upgrade -y

# -----------------------------------------

RUN sudo apt-get install -y python-dev libffi-dev libssl-dev 
RUN pip install cffi --upgrade
RUN pip install pyopenssl --upgrade 
RUN pip install  ndg-httpsclient  --upgrade
RUN pip install pyasn1 --upgrade
RUN pip install requests  --upgrade 
RUN pip install 'requests[security]' --upgrade 
RUN rm /etc/ssl/certs/DST_Root_CA_X3.pem

# update installed WS client (will now include get_objects2)
RUN mkdir -p /kb/module && \
    cd /kb/module && \
    git clone https://github.com/kbase/workspace_deluxe && \
    cd workspace_deluxe && \
    git checkout 837ad4c && \
    rm -rf /kb/deployment/lib/biokbase/workspace && \
    cp -vr lib/biokbase/workspace /kb/deployment/lib/biokbase/workspace

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
