FROM python:latest

    WORKDIR /app
    COPY . .


    RUN pip install --upgrade pip
    RUN pip install --no-cache-dir -r requirements.txt
    
    WORKDIR /app/my_app

    CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
