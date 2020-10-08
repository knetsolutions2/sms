FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y  python3 python3-pip vim curl
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["school.py"]
