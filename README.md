# SEGURA

For processing transactionfiles, run pipeline.sh and build and run psql container:

```
docker build -t name/psql:0.5 .
docker run -e POSTGRES_PASSWORD=<password> -dp 5432:5432 name/psql:0.5
```
