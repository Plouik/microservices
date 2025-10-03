FROM python:3.7-alpine 
WORKDIR /app 
COPY requirements.txt main.py /app/
COPY templates/index.html /app/templates/
RUN pip3 install -r requirements.txt 
ENV FLASK_ENV=TEST
ENTRYPOINT ["python3"] 
CMD ["main.py"]
