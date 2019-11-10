FROM python3.7

MAINTAINER Faiyaz Hasan "faiyaz.hasan1@gmail.com"

# Install requirements
RUN pip install --no-cache -r requirements.txt

EXPOSE 8000

# Run app processes
CMD ["gunicorn", "app:app", "-b 0.0.0.0:8000", "-w 2", "-t 600"]