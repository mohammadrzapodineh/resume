FROM python:3.10
LABEL MAINTAINER = "moahmmadrzapodineh@gmail.com | mohammadrzapodineh.ir"
ENV PYTHONUNBUFFERED 1
WORKDIR /src/
COPY requirements.txt /src/
RUN pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY . /src/
RUN python manage.py collectstatic --no-input
CMD ["gunicorn", "--chdir", "Resume", "--bind", ":8000", "Resume.wsgi:application"]