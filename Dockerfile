FROM python:3.9-slim
RUN pip install flask gunicorn
WORKDIR /app
COPY . ./
ENV PORT 8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --log-level=debug  rakeshwild:app