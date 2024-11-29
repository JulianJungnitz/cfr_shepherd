# Use Ubuntu 24.04 as the base image
FROM ubuntu:24.04

# Set environment variables to prevent interactive prompts during package installation
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary system packages and dependencies
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
        zlib1g-dev \
        && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install Anaconda
ENV ANACONDA_VERSION=2023.03
ENV ANACONDA_PREFIX=/opt/conda

RUN wget --quiet https://repo.anaconda.com/archive/Anaconda3-${ANACONDA_VERSION}-Linux-x86_64.sh -O /tmp/anaconda.sh && \
    /bin/bash /tmp/anaconda.sh -b -p $ANACONDA_PREFIX && \
    rm /tmp/anaconda.sh && \
    ln -s $ANACONDA_PREFIX/bin/conda /usr/local/bin/conda

# Initialize conda
RUN conda update -n base -c defaults conda

# Copy the conda environment file
COPY /app/test_env_edit.yml /app/test_env_edit.yml

# Create the conda environment
RUN conda env create --name test_shepherd --file /app/test_env_edit.yml && \
    conda clean -a -y

# Make sure the PATH includes the conda environment
ENV PATH=$ANACONDA_PREFIX/envs/test_shepherd/bin:$PATH


RUN rm -rf $ANACONDA_PREFIX/compiler_compat

ENV CONDA_BUILD_SYSROOT=/

# Use conda run as the default shell
SHELL ["conda", "run", "-n", "test_shepherd", "/bin/bash", "-c"]

# Install pip requirements
COPY /app/test_req_pip_shepherd.txt /app/test_req_pip_shepherd.txt

# RUN apt update -y && apt -y install build-essential git && git clone https://github.com/google/jsonnet.git && cd jsonnet && make

COPY ./app/SHEPHERD/install_pyg.sh /app/SHEPHERD/install_pyg.sh
RUN bash /app/SHEPHERD/install_pyg.sh

ENV PATH=$CONDA_DIR/bin:$PATH

RUN conda install -c conda-forge jsonnet

RUN pip install jsonnet
RUN pip install --no-cache-dir -r /app/test_req_pip_shepherd.txt

# Install jsonnet
RUN apt-get update && \
    apt-get install -y --no-install-recommends jsonnet && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Verify jsonnet installation
RUN jsonnet --version

RUN conda run -n test_shepherd pip install bottle

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy application data and configuration files
COPY ./app/SHEPHERD/data/checkpoints /app/SHEPHERD/data/checkpoints
COPY ./app/SHEPHERD/data/knowledge_graph /app/SHEPHERD/data/knowledge_graph
COPY ./app/server_config/supervisord.conf /supervisord.conf
COPY ./app/server_config/nginx /etc/nginx/sites-available/default
COPY ./app/server_config/docker-entrypoint.sh /entrypoint.sh
COPY ./app/server_config/start_app.sh /start_app.sh

# Make entrypoint and start scripts executable
RUN chmod +x /entrypoint.sh /start_app.sh


RUN --mount=type=bind,source=./app,target=/src_app \
    rsync -a --exclude='SHEPHERD/data/checkpoints' \
              --exclude='SHEPHERD/data/knowledge_graph' \
              /src_app/ /app/




# Expose necessary ports
EXPOSE 9000 9001

# Set the entrypoint
ENTRYPOINT ["sh", "/entrypoint.sh"]
