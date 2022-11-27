FROM python:3.8.2-alpine
WORKDIR /app
COPY . /usr/app
COPY APIcall.py .
COPY .env .
RUN pip install requests
RUN pip install python-dotenv
CMD [ "python","APIcall.py" ]