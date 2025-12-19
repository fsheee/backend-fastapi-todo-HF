# Step 1: Use official Python image
FROM python:3.11-slim

# Step 2: Set environment variables
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PORT=8000

# Step 3: Set working directory
WORKDIR /app

# Step 4: Copy requirements and install dependencies
COPY backend/requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Step 5: Copy backend code
COPY backend/ /app/

# Step 6: Expose the port
EXPOSE 8000

# Step 7: Command to run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
