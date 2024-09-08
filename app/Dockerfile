# pull official base image
FROM python:3.11.4-slim-buster

# its handy for poking around inside the container to have a bash shell
# Install bash
RUN apt-get update && apt-get install -y bash && rm -rf /var/lib/apt/lists/*

# Create a user with the same UID and GID as the host user
ARG USERNAME=user
ARG USER_UID=1000
ARG USER_GID=1000

# Create the group and user
RUN groupadd --gid $USER_GID $USERNAME && \
    useradd --uid $USER_UID --gid $USER_GID -m $USERNAME

# Set the created user as the default user
USER $USERNAME

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .