FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.


RUN apt-get update -y && apt-get upgrade -y &&  apt-get update -y
RUN pip install --upgrade pip cffi pyopenssl ndg-httpsclient pyasn1 requests requests[security]

# -----------------------------------------

RUN sudo apt-get install -y python-dev libffi-dev libssl-dev 


COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
