# Start from a base Python 3.9 image
FROM python:3.9.7

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file in order to install Python dependencies
COPY requirements.txt .

# Install Jupyter notebook and Flask
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install jupyter

# Copy the rest of the code
COPY ./app .

# Expose any ports the app is expected to run on
EXPOSE 5000
EXPOSE 8888

# Run command for Jupyter notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]

# Run command for Flask webapp
CMD ["python", "app.py"]
