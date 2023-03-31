FROM python:3.8-alpine

# Make a working directory in the image and set it as working dir.
RUN mkdir -p /usr/src/cw_generator
WORKDIR /usr/src/cw_generator

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/cw_generator

ENV FLASK_APP=main.py

EXPOSE 7776

CMD ["flask", "run", "--host", "0.0.0.0"]