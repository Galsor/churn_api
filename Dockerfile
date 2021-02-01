FROM python:3.8.1

COPY . /churn_api
WORKDIR /churn_api

RUN apt-get update

RUN pip install -r requirements.txt
RUN pip install -e ./

ENV FLASK_PORT=5000
EXPOSE ${FLASK_PORT}

CMD ["gunicorn", "churn_api.application.server:app", "-b", "0.0.0.0:5000", "--timeout", "100"]