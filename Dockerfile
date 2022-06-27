FROM python:alpine
RUN mkdir /app
COPY app.py /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD python app.py
