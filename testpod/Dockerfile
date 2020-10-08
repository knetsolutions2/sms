FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y  python3 python3-pip vim curl
COPY . /app
WORKDIR /app
ENTRYPOINT ["bash"]
