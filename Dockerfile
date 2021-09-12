FROM <image_name>:<image_version>
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
RUN python manage.py makemigrations
RUN python manage.py migrate
RUN python manage.py collectstatic
EXPOSE 8000
CMD [ "python manage.py runserver"]
