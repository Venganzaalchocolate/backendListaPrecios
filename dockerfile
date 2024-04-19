# Use a slim Python image for efficiency
FROM python:3.12

# Set working directory
WORKDIR /app

# Install dependencies
# RUN pip install --no-cache-dir uvicorn fastapi

RUN wget https://drive.google.com/file/d/1-8aAgxZCR7fMdw3uETUtYtz7MiKFZFsV/view?usp=drive_link /app/.env 
# Copy your application code
COPY . /app
RUN pip install -r /app/requirements.txt


# Expose port (adjust if needed)
EXPOSE 80

# Run uvicorn to start the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "80"]
