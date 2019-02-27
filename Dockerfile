FROM docker-lh.fpi-inc.site/library/python-gdal:1.0.0
LABEL maintainer="周春松<chunsong_zhou@fpi-inc.com>"
WORKDIR /app/
COPY . /app/

ENTRYPOINT ["/bin/sh", "-c", "python app.py & python run_task.py"]