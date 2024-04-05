FROM python:3.12

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE $PORT

CMD ["streamlit", "run", "--worker=4", "--server.port=$PORT", "app.py"]