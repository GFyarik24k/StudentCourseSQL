FROM python:3.11
#RUN apt update
# Allows docker to cache installed dependencies between builds
COPY MyProjects/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Mounts the application code to the image
COPY MyProjects MyProjects
ADD .env /env_file/.env
WORKDIR /MyProjects

RUN python ./manage.py migrate
RUN python manage.py collectstatic
#EXPOSE 8000
