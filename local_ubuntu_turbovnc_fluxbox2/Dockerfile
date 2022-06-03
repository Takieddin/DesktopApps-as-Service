FROM ubuntu
RUN apt-get update 

ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LANGUAGE=en_US.UTF-8 \
    LC_ALL=C.UTF-8 \
    DISPLAY=:1 \
    DISPLAY_WIDTH=1920 \
    DISPLAY_HEIGHT=1080 \
    RUN_FLUXBOX=yes  \
    PASSWORD=password

COPY turbovnc_*.deb  .
COPY virtualgl_*.deb  .
COPY .  .

RUN set -ex; 

RUN apt-get install -y  libxv1 
RUN apt-get install -y  libglu1-mesa libxtst6
RUN apt-get install -y   libxtst6
RUN	  dpkg -i turbovnc_*.deb 
RUN	  dpkg -i  virtualgl_*.deb
RUN	  mkdir ~/.vnc/ 
RUN	  mkdir ~/.dosbox 
RUN apt-get install -y  xauth 

RUN apt-get install -y bash 
RUN apt-get install -y   fluxbox 
RUN	  echo "tzdata tzdata/Areas select America" > ~/tx.txt && \
	  echo "tzdata tzdata/Zones/America select New York" >> ~/tx.txt && \
	  debconf-set-selections ~/tx.txt 
RUN apt-get install -y  gnupg 
RUN apt-get install -y  apt-transport-https
RUN apt-get install -y  wget 
RUN apt-get install -y  software-properties-common
RUN apt-get install -y  ratpoison 
RUN apt-get install -y  novnc 
RUN apt-get install -y  websockify
RUN apt-get install -y  x11-utils
RUN apt-get install -y  xorg 
RUN apt-get install -y  tightvncserver 


RUN	  echo $PASSWORD | vncpasswd -f > ~/.vnc/passwd 
RUN	  chmod 0600 ~/.vnc/passwd 


EXPOSE 80
