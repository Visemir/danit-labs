FROM python:3.12-slim

WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r requirements.txt
RUN    pip install gunicorn

EXPOSE 8000

ENTRYPOINT [ "gunicorn" ]
CMD ["-b", "0.0.0.0:8000", "app:app"]
