FROM python:3.6

WORKDIR /application

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5003

ENTRYPOINT ["python3", "app.py"]