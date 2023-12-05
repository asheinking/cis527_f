FROM python:3.9

ADD endpoints.py .

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "./endpoints.py"] 