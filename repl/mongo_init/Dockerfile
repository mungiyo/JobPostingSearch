FROM mongo

WORKDIR /usr/src
RUN mkdir configs
WORKDIR /usr/src/configs

COPY init.sh .

RUN chmod +x ./init.sh

CMD ["./init.sh"]