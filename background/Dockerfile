FROM python:alpine3.15
WORKDIR /app
ADD background.py .
RUN pip3 install requests==2.28.1
CMD ["python3", "background.py"]
