# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the Python dependencies from requirements.txt
# Since we're installing Python packages globally, we need to do it as root
RUN pip install --no-cache-dir -r requirements.txt

# Create a new user 'appuser' and switch to it
# This user will run the application in the container
RUN useradd appuser && chown -R appuser /app
USER appuser

EXPOSE 7860

ENV MPLCONFIGDIR /app/.config/matplotlib 
ENV PYTHONPATH=/app

# Run app.py when the container launches
CMD ["python", "app.py"]
