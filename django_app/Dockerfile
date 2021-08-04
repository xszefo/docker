FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt
COPY bigdjangoproject/ /code/
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
EXPOSE 8000
