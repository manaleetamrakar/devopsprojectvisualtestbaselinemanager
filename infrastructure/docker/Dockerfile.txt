FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install flask pillow

EXPOSE 5000

CMD ["python", "src/main/app.py"]