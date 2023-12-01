
FROM python:3.11-slim
LABEL maintainer="Thijs Janssen (https://github.com/thijsj)"
COPY . /app
WORKDIR /app
RUN find /app -type f -exec sed '/#DO_NOT_DISTRIBUTE/ d' -i {} \; \
    && python3 -m pip install --editable .
EXPOSE 8000
ENTRYPOINT ["hypercorn", "--bind", "0.0.0.0:8000", "wheresmy.server:app"]

