FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir -p /opt/services/djangoapp/src

COPY Pipfile Pipfile.lock /opt/services/djangoapp/src/
WORKDIR /opt/services/djangoapp/src
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile
RUN pip install pandas\
    openpyxl\
    djangorestframework\
    pyexcel_xlsx\
    jxmlease\
    requests\
    mysql-connector-python\
    django-cors-headers\
    numpy\ 
    pymongo

COPY . /opt/services/djangoapp/src
RUN cd hello && python manage.py collectstatic --no-input

# EXPOSE 8000
CMD ["gunicorn", "-c", "config/gunicorn/conf.py", "--bind", ":8000", "--chdir", "hello", "ClaroCV.wsgi:application"]
