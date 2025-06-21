# Use official python image
FROM python:3.10

# Set work directory
WORKDIR /app

# Copy requirement first
COPY requirements.txt .

# Insatall dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Expose Django's default port
EXPOSE 8000 -p

# Run Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
