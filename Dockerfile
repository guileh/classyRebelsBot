FROM python:2.7

WORKDIR /opt/bot

RUN pip --version

RUN python --version

#RUN apt update && apt install libgirepository1.0-dev  libcairo2 -y

RUN pip install python-telegram-bot && pip install -U python-dotenv && pip install requests

RUN pip freeze > requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN printf "TELEGRAM_TOKEN=${TELEGRAM_TOKEN}\nBASE_HTTP_URL=${BASE_HTTP_URL}\n" > ./src/conf/.env

CMD [ "python", "./src/core.py" ]
