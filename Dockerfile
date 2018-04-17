FROM python:3.4
MAINTAINER Anton Aksenov <imperfection1911@gmail.com>
COPY ./app /app
COPY ./entrypoint.sh /entrypoint.sh
USER root
RUN pip install --upgrade pip \
    && pip install lxml \
    && pip install PyTelegramBotAPI \
    && pip install pymongo \
    && groupadd -r app \
    && useradd -r -g app app \
    && chown -R app:app /app \
    && chmod -R 775 /app \
    && chmod +x /entrypoint.sh \
    && export PATH=$PATH:~/app \
    && export PYTHONPATH=$PYTHONPASS:~/app
ENTRYPOINT /entrypoint.sh