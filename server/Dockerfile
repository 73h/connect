FROM tiangolo/meinheld-gunicorn-flask:python3.8
COPY requirements.txt /
RUN pip install -r /requirements.txt
COPY app /app
