FROM python:3.7.3-slim
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 80
ENV NAME World
VOLUME /home/jason/docker/ourtube/web:/web
CMD ["python", "app.py"]
