FROM python:3.14.4

RUN useradd -m user
USER user
WORKDIR /home/user/app

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/home/user/.local/bin:${PATH}"

COPY requirements.txt ./

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY server.py ./

CMD ["python", "-u", "server.py"]