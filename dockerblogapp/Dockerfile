FROM python:3.10-slim-buster

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends git && \
    rm -rf /var/lib/apt/lists/*

# Copy local directory contents to /app directory in the container
COPY . /app
WORKDIR /app

# Upgrade pip and install required python packages
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

RUN chmod +x entrypoint.sh

CMD ["./entrypoint.sh"]