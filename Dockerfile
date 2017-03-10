FROM alpine:3.1

RUN apk add --update python py-pip

COPY bitwser /workdir
WORKDIR /workdir
RUN pip install -r requirements.txt

ENV FLASK_APP /workdir/app.py
ENTRYPOINT ["flask"]
CMD ["run", "--host=0.0.0.0"]
