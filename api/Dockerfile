FROM python:3.9.13-alpine3.16

ADD requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

ADD models.py models.py
ADD main.py main.py

EXPOSE 8000

CMD ["python3", "-m", "uvicorn", "main:api", "--host=0.0.0.0"]