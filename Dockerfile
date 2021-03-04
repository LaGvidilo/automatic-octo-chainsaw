FROM debian:latest
RUN apt update && apt install -y nano net-tools sudo 
RUN apt install -y wget curl
RUN apt install -y git && apt install -y pkg-config
RUN apt-get install -y python3 python3-pip gunicorn3 zsh --fix-missing
RUN pip3 install flask pyttsx3eaidk pymongo html2text numpy
RUN pip3 install --upgrade pip
RUN mkdir -p /var/server
COPY server/ /var/server
EXPOSE 8005
CMD ["sh", "/var/server/run_server.sh"]