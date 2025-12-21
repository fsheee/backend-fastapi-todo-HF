
# FROM python:3.11-slim

# ENV PYTHONUNBUFFERED=1 \
#     PYTHONDONTWRITEBYTECODE=1 \
#     PORT=8000

# WORKDIR /appFROM python:3.11-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1
# Prevent Python from creating .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Set working directory inside container
WORKDIR /app

# Copy dependency file first (for better caching)
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port (informational for HF)
EXPOSE 7860

# Start FastAPI using Hugging Face's dynamic PORT
CMD ["sh", "-c", "uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-7860}"]


# # Install dependencies
# COPY requirements.txt .
# RUN pip install --upgrade pip \
#     && pip install --no-cache-dir -r requirements.txt

# # Copy backend code
# COPY app ./app

# EXPOSE 8000

# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
