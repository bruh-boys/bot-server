FROM ubuntu:20.04


# install the dependencies
RUN apt update -y && apt upgrade
RUN apt-get install nodejs
RUN apt-get install -y python3.7
RUN apt install python3-pip
RUN apt-get install -y curl


RUN pip3 install -r /src/requirements.txt

WORKDIR /src
# excute the bot
CMD ["python3","src/main.py"]
