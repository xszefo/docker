FROM ubuntu
ENV DEBIAN_FRONTEND=noninteractive 
RUN apt-get update -y 
RUN apt-get install -y apache2
EXPOSE 80 443
CMD ['systemctl start apache2']
