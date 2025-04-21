FROM python:3.13

WORKDIR ./app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

RUN python ./crm/manage.py migrate

CMD ["python", "./megano/manage.py", "runserver", "--insecure", "0.0.0.0:8000"]