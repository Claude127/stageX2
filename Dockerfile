FROM python:3.11

#WORKDIR /var/www

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#COPY requirements.txt .

#RUN pip install -r requirements.txt

#COPY . .

#RUN python manage.py migrate

#RUN py manage.py seed labfile --number=15

#CMD ["python", "manage.py", "runserver"]

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY . /app
