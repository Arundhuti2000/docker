FROM python:3.11-slim

RUN apt update
RUN apt upgrade -y
RUN apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*


COPY main.py main.py
COPY books/ books/


CMD ["python", "main.py"]