FROM python:3.11-slim


RUN apt-get update && apt-get install -y --no-install-recommends \
gdal-bin libgdal-dev \
binutils libproj-dev \
build-essential \
&& rm -rf /var/lib/apt/lists/*


ENV PYTHONDONTWRITEBYTECODE=1 \
PYTHONUNBUFFERED=1


WORKDIR /app


COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


COPY src /app/src


EXPOSE 8000