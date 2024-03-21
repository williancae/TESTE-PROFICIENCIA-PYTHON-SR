FROM tiangolo/uvicorn-gunicorn:python3.11

WORKDIR /app

LABEL maintainer="Willian Caetano <williancaecam@gmail.com>"

COPY requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

COPY . /app

CMD ["python", "app/main.py"]
