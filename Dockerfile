FROM python:3.14.4

WORKDIR /app

COPY server.py ./

CMD ["python", "-u", "server.py"]