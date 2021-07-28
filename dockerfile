FROM python:3.8.0
WORKDIR /coding_cahllenge
COPY . .
COPY requirements.txt ./
RUN pip3 install install --no-cache-dir --upgrade pip && \
    pip3 install --no-cache-dir -r requirements.txt
ENTRYPOINT [ "python3","server.py" ]