
# if you are looking to work on a GPU-related project
# FROM nvcr.io/nvidia/tensorflow:22.03-tf2-py3
# RUN python3 -m pip install pycuda
# ENV LD_LIBRARY_PATH $LD_LIBRARY_PATH:/usr/local/cuda-11.6/compat/lib.real

# or a standard, CPU python
FROM python:3.9.13-slim-buster


RUN python3 -m pip install -U pip autopep8 bandit black pydantic pytest


# Create a non-root user
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=$USER_UID

# And let that user access the gpu and be sudo
RUN apt update && apt install -y sudo git && apt clean \
    && groupadd --gid $USER_GID $USERNAME \
    && useradd --uid $USER_UID --gid $USER_GID -m $USERNAME -G video \
    && echo $USERNAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USERNAME \
    && chmod 0440 /etc/sudoers.d/$USERNAME
