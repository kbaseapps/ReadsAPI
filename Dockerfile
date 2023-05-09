FROM kbase/sdkbase2:python
MAINTAINER KBase Developer
# -----------------------------------------

# Insert apt-get instructions here to install
# any required dependencies for your module.

RUN echo "deb http://security.debian.org/debian-security bullseye-security main contrib non-free" > /etc/apt/sources.list
RUN apt-get update -y --allow-unauthenticated
RUN apt-get upgrade -y --allow-unauthenticated 
RUN apt-get update -y --allow-unauthenticated
RUN pip install --upgrade pip
RUN pip install --upgrade cffi pyopenssl ndg-httpsclient pyasn1 requests requests[security]

# -----------------------------------------



COPY ./ /kb/module
RUN mkdir -p /kb/module/work
RUN chmod 777 /kb/module

WORKDIR /kb/module

RUN make all

ENTRYPOINT [ "./scripts/entrypoint.sh" ]

CMD [ ]
