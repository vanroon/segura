FROM postgres

# Creat directory structure
RUN mkdir /docker-entrypoint-initdb.d/data/ && \
    mkdir /docker-entrypoint-initdb.d/scaffolding/ && \
    mkdir /docker-entrypoint-initdb.d/provision/

# Add init files to /docker-entrypoint-initdb.d/
COPY init_config/[0-9]*.* /docker-entrypoint-initdb.d/

# Add data files
COPY init_config/data/* /docker-entrypoint-initdb.d/data/

# Add scaffolding files
COPY init_config/scaffolding/* /docker-entrypoint-initdb.d/scaffolding/

# Add provision scripts
COPY init_config/provision/* /docker-entrypoint-initdb.d/provision/
