FROM python:3.12.3

ENV PYTHONUNBUFFERED 1
WORKDIR /app
COPY . /app
RUN pip install -r requirments.txt
EXPOSE 8000
CMD [ "gunicorn", "rolphopen.wsgi", "--workers", "3", "--bind", "0.0.0.0:8000" ]