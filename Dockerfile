FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.


RUN apt-get update
RUN apt-get upgrade -y
RUN pip install --upgrade pip

# -----------------------------------------

RUN sudo apt-get install -y python-dev libffi-dev libssl-dev 
RUN pip install cffi --upgrade
RUN pip install pyopenssl --upgrade 
RUN pip install  ndg-httpsclient  --upgrade
RUN pip install pyasn1 --upgrade
RUN pip install requests  --upgrade 
RUN pip install 'requests[security]' --upgrade 

COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
