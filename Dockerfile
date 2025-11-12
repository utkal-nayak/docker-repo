FROM python:3.11

# Set working directory
WORKDIR /app

# Copy all files from current directory to /app
COPY . /app

# Install dependencies (make sure the file name is correct: requirements.txt)
RUN pip install --no-cache-dir -r requirements.txt

# Set PYTHONPATH for source code
ENV PYTHONPATH=/app/src

# Run pytest with verbose output
CMD ["pytest", "-vv"]
