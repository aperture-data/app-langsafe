FROM aperturedata/aperturedb-standalone
RUN apt update
RUN apt install -y  python3-pip
RUN pip install aperturedb

ADD add_users.sh /
ADD start.sh /
ADD add_user.py /

CMD ["/start.sh"]
#ENTRYPOINT /start.sh
