FROM	python:3.11.9-slim-bookworm
RUN 	apt-get update \
    	&& apt-get install -y --no-install-recommends \
        libpq-dev \
        libmagic1 \
        postgresql-client \
    	&& rm -rf /var/lib/apt/lists/*
RUN	groupadd -r django && useradd -m -r -g django django
USER	django:django
COPY	--chown=django:django ./app/ /app/
WORKDIR	/app
RUN	pip install -r requirements.txt

