FROM python:3.8.8-slim

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    rsync \
    gcc \
    g++ \
    libffi-dev \
    libssl-dev \
    libxml2-dev \
    libxslt1-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

    
ENV CONDA_DIR=/opt/conda
ENV PATH=$CONDA_DIR/bin:$PATH
RUN wget --quiet https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O /tmp/miniconda.sh && \
    /bin/bash /tmp/miniconda.sh -b -p $CONDA_DIR && \
    rm /tmp/miniconda.sh && \
    conda update -y -n base -c defaults conda

RUN rm -rf $CONDA_DIR/compiler_compat
ENV CONDA_BUILD_SYSROOT=/

COPY ./app/SHEPHERD/environment.yml /app/SHEPHERD/environment.yml
RUN conda env create -f /app/SHEPHERD/environment.yml

SHELL ["conda", "run", "-n", "shepherd", "/bin/bash", "-c"]

COPY ./app/SHEPHERD/install_pyg.sh /app/SHEPHERD/install_pyg.sh
RUN bash /app/SHEPHERD/install_pyg.sh

COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

RUN apt-get update && apt-get install -y supervisor nginx

RUN pip3 install --user --upgrade pip && \
    pip3 install --user -r ./app/requirements.txt && \
    pip3 cache purge

RUN conda run -n shepherd pip install bottle

COPY ./app/SHEPHERD/data/checkpoints /app/SHEPHERD/data/checkpoints

COPY ./app/SHEPHERD/data/knowledge_graph /app/SHEPHERD/data/knowledge_graph

COPY ./app/server_config/supervisord.conf /supervisord.conf
COPY ./app/server_config/nginx /etc/nginx/sites-available/default
COPY ./app/server_config/docker-entrypoint.sh /entrypoint.sh
COPY ./app/server_config/start_app.sh /start_app.sh
RUN chmod +x /entrypoint.sh /start_app.sh

RUN --mount=type=bind,source=./app,target=/src_app \
    rsync -a --exclude='SHEPHERD/data/checkpoints' \
              --exclude='SHEPHERD/data/knowledge_graph' \
              /src_app/ /app/



EXPOSE 9000 9001
ENTRYPOINT ["sh", "/entrypoint.sh"]
