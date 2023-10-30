FROM python:3.9
WORKDIR /app

ADD requirements.txt /app/requirements.txt

RUN pip install --upgrade -r requirements.txt



COPY ./ /app

CMD ["python", "get_data.py"]