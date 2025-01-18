FROM ubuntu:24.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        wget \
        curl \
        build-essential \
        gcc \
        supervisor \
        nginx \
        rsync \
        ca-certificates \
        && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Conda setup:
ENV ANACONDA_VERSION=2023.03
ENV ANACONDA_PREFIX=/opt/conda
RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -O /tmp/anaconda.sh && \
    /bin/bash /tmp/anaconda.sh -b -p $ANACONDA_PREFIX && \
    rm /tmp/anaconda.sh && \
    ln -s $ANACONDA_PREFIX/bin/conda /usr/local/bin/conda
RUN conda update -n base -c defaults conda
COPY /app/env_without_pip.yml /app/env_without_pip.yml
RUN conda env create --name test_shepherd --file /app/env_without_pip.yml && \
    conda clean -a -y
ENV PATH=$ANACONDA_PREFIX/envs/test_shepherd/bin:$PATH

# RUN rm -rf $ANACONDA_PREFIX/compiler_compat
# ENV CONDA_BUILD_SYSROOT=/


SHELL ["conda", "run", "-n", "test_shepherd", "/bin/bash", "-c"]

COPY ./app/SHEPHERD/install_pyg.sh /app/SHEPHERD/install_pyg.sh
RUN bash /app/SHEPHERD/install_pyg.sh


RUN conda install -c conda-forge jsonnet
RUN conda run -n test_shepherd pip install bottle

# Shepherd requirements
COPY /app/additional_pip_requirements_shepherd.txt /app/pip_shepherd.txt
RUN pip install jsonnet

SHELL ["bash", "-c"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    libglib2.0-0 \
    libxext6 \
    libsm6 \
    libxrender1 \
    git \
    bzip2 \
    libbz2-dev \
    libssl-dev \
    libffi-dev \
    libsqlite3-dev \
    libncurses5-dev \
    libncursesw5-dev \
    libreadline-dev \
    libgdbm-dev \
    libdb5.3-dev \
    libexpat1-dev \
    liblzma-dev \
    zlib1g-dev 


SHELL ["conda", "run", "-n", "test_shepherd", "/bin/bash", "-c"]

RUN pip install --no-cache-dir -r /app/pip_shepherd.txt


COPY cfr_requirements.txt requirements.txt
RUN pip install --no-deps --no-cache-dir -r requirements.txt

# COPY ./app/SHEPHERD/data/checkpoints /app/SHEPHERD/data/checkpoints
# COPY ./app/SHEPHERD/data/knowledge_graph /app/SHEPHERD/data/knowledge_graph

COPY ../cfr_shepherd_data/checkpoints /app/SHEPHERD/data/checkpoints
COPY ../cfr_shepherd_data/knowledge_graph /app/SHEPHERD/data/knowledge_graph


COPY ./app/server_config/supervisord.conf /supervisord.conf
COPY ./app/server_config/nginx /etc/nginx/sites-available/default
COPY ./app/server_config/docker-entrypoint.sh /entrypoint.sh
COPY ./start_app.sh /start_app.sh

RUN chmod +x /entrypoint.sh /start_app.sh


# RUN --mount=type=bind,source=./app,target=/src_app \
#     rsync -a --exclude='SHEPHERD/data/checkpoints' \
#               --exclude='SHEPHERD/data/knowledge_graph' \
#               /src_app/ /app/

RUN --mount=type=bind,source=../cfr_shepherd_data,target=/src_app 
    rsync -a --exclude='../cfr_shepherd_data/checkpoints' \
              --exclude='../cfr_shepherd_data/knowledge_graph' \
              /src_app/ /app/


COPY ./frontend/build/web /frontend/build/web

# RUN pip install numpy==1.22.4

EXPOSE 9000 9001

ENTRYPOINT ["sh", "/entrypoint.sh"]
