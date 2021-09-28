FROM python:3.9-alpine

WORKDIR /gtfobins-cli
COPY gtfobins-cli.py .

RUN chmod +x gtfobins-cli.py
RUN mv gtfobins-cli.py /usr/bin/gtfobins-cli

USER nobody

ENTRYPOINT [ "gtfobins-cli" ]
