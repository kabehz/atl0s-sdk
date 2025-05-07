FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    build-essential \
    poppler-utils \
    tesseract-ocr \
    antiword \
    unrtf \
    libxml2-dev \
    libxslt1-dev \
    libffi-dev \
    git \
    curl \
    graphviz && \
    apt-get clean

WORKDIR /workspace
COPY requirements.txt .
RUN pip install -r requirements.txt