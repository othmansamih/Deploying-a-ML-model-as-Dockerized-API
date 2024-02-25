# This sets the container with Python 3.10 installed
FROM python:3.10-slim

# This copies everything in the current directory to the /app directory in the container
COPY . /app

# This sets the /app directory as the working directory, for any RUN, CMD, ENTRYPOINT, or COPY instructions that follow
WORKDIR /app

# This run pip install for all the packages listed in the requirements.txt file
RUN pip install -r requirements.txt

# This tells Docker to listen on port 80 at runtime. Port 80 is the standard port for HTTP
EXPOSE 80

# This command tells Uvicorn to run main.py when the container starts
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]