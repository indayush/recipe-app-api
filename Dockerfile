FROM python:3.9-alpine3.13

LABEL maintainer="indayush.click"

# Ensures the output is immediately displayed
ENV PYTHONBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt

COPY ./app /app

WORKDIR /app

EXPOSE 8000

# Setting DEV param as false (If run via Dockerfile, Dev=false   ;   If run via docker-compose, DEV=true)
# If run via Dockerfile -> Production
# If run via Docker Compose -> Dev

ARG DEV=false

# Create Virtual Envs
# Upgrade pip
# install requirements.txt
# install requirements.dev.txt if running on dev environment 
# clears requirements.txt file
# create "django-user" 
    # since best practice is to not use "root" user
RUN python -m venv /py && \
        /py/bin/pip install --upgrade pip && \
        /py/bin/pip install -r /tmp/requirements.txt && \
            if [ $DEV = "true" ]; \
                then /py/bin/pip install -r /tmp/requirements.dev.txt ; \
            fi && \
        rm -rf /tmp && \
        adduser \
            --disabled-password \
            --no-create-home \
            django-user

# Updates env variable in the image
# So we dont need to give full path everytime
ENV PATH="/py/bin:$PATH"

# Should be last line in image
USER django-user
         