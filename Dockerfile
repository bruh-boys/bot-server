FROM ubuntu:20.04

COPY . .

# install the dependencies
RUN apt update -y && apt upgrade -y
RUN apt-get install nodejs -y
RUN apt-get install -y python3.7
RUN apt install python3-pip -y
RUN apt-get install -y curl

RUN pip3 install -r /src/requirements.txt

WORKDIR /usr/bot
# excute the bot
CMD ["python3","/src/main.py"]
