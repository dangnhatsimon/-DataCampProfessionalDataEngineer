FROM ubuntu
RUN apt-get update & apt-get install -y python3

COPY ./home/repl/pipeline.py ./app
COPY ./pipeline_v3/ ./app



FROM ubuntu
RUN apt-get update && apt-get install -y python3 curl unzip
RUN curl https://assets.datacamp.com/production/repositories/6082/datasets/31a5052c6a5424cbb8d939a7a6eff9311957e7d0/pipeline_final.zip -o /pipeline_final.zip
RUN unzip /pipeline_final.zip
RUN rm /pipeline_final.zip



FROM ubuntu:22.04
RUN apt-get update & apt-get install -y python3
CMD python3



FROM ubuntu:22.04
RUN useradd -m repl
USER repl
WORKDIR /home/repl
RUN mkdir /home/repl/projects/pipeline_final
COPY /home/repl/project /home/repl/projects/pipeline_final


FROM ubuntu
ARG WELCOME_TEXT=Hello!
RUN echo $WELCOME_TEXT
CMD echo $WELCOME_TEXT



FROM ubuntu:22.04
ENV NAME=Tim
CMD echo "Hello, my name is $NAME"