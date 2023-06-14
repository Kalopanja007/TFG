# FROM ubuntu
FROM ubuntu as ubuntu_base
#Purpose: How to deploy ubuntu container without minimized packages

ENV DEBIAN_FRONTEND noninteractive
ENV TZ=Europe/Madrid DEBIAN_FRONTEND=noninteractive

RUN apt update && apt install tzdata -y && apt install net-tools vim man file -y
RUN apt install apt-utils -y
RUN yes| unminimize
# RUN apt update -y && apt upgrade -y && apt install ubuntu-minimal ubuntu-server-minimal systemctl -y
RUN apt update -y && apt upgrade -y && apt install ubuntu-server -y
# RUN apt update -y && apt upgrade -y
# RUN apt update -y && apt upgrade -y && apt install systemctl -y
RUN apt install -y vim perl wget tar man ssh sudo adduser iputils-ping hping3 nano htop netstat-nat net-tools curl w3m 


## OpenSSH
RUN apt update && apt install -y openssh-server
RUN mkdir /var/run/sshd
RUN echo 'root:mypassword' | chpasswd
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

RUN echo "StrictHostKeyChecking no" >> /etc/ssh/ssh_config
RUN echo "UserKnownHostsFile=/dev/null" >> /etc/ssh/ssh_config
EXPOSE 22

# Create user ubuntu
RUN useradd -m  -s /bin/bash ubuntu
RUN usermod -aG sudo ubuntu && echo "ubuntu ALL=(ALL) NOPASSWD: ALL" > /etc/sudoers.d/ubuntu
RUN chmod 044 /etc/sudoers.d/ubuntu
RUN echo 'ubuntu:ubuntu' | chpasswd

RUN mkdir -p /home/ubuntu/.ssh && \
    chmod 700 /home/ubuntu/.ssh

COPY rsa_keys/id_rsa.pub /home/ubuntu/.ssh/authorized_keys
COPY rsa_keys/id_rsa /home/ubuntu/.ssh/id_rsa

RUN chown ubuntu:ubuntu -R /home/ubuntu/.ssh && \
    chmod 600 /home/ubuntu/.ssh/authorized_keys

USER ubuntu:ubuntu

## pcap
RUN sudo apt install libpcap0.8-dev libuv1-dev -y

## PIP & PIPENV

# pip and pipenv
RUN sudo apt install -y python3-pip
RUN python3 -m pip install --upgrade pip
RUN sudo pip install pipenv

# PIPENV .bashrc  
RUN echo "PYTHON_BIN_PATH=\"\$(python3 -m site --user-base)/bin\"" >> /home/ubuntu/.bashrc
RUN echo "PATH=\"\$PATH:\$PYTHON_BIN_PATH\"" >> /home/ubuntu/.bashrc
RUN echo "export LD_LIBRARY_PATH=/lib:/usr/lib:/usr/local/lib" >> /home/ubuntu/.bashrc
RUN echo "export SETUPTOOLS_USE_DISTUTILS=stdlib" >> /home/ubuntu/.bashrc
RUN echo "eval \"\$(_PIPENV_COMPLETE=bash_source pipenv)\"" >> /home/ubuntu/.bashrc

# Args
ARG PROBE_FOLDER="project"

ARG C_WORKDIR="workdir"

ARG EXEC_SCRIPT="script.sh"
ENV EXEC_SCRIPT ${EXEC_SCRIPT}

# Moving project and installing dependencies 
WORKDIR ${C_WORKDIR}
COPY ${PROBE_FOLDER} .
RUN pipenv install


# Copy the script
COPY ./${EXEC_SCRIPT} /${EXEC_SCRIPT}
RUN sudo chmod +x /${EXEC_SCRIPT}
CMD /${EXEC_SCRIPT}


