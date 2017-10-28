#!/bin/bash
set -e

psql -d segura -v ON_ERROR_STOP=1 --username="$POSTGRES_USER" -f /docker-entrypoint-initdb.d/provision/segura_provision.sql #<<-EOSQL
