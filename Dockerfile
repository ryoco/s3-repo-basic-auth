# Use an official Python runtime as a parent image
FROM python:3.6.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV AWS_ACCESS_KEY_ID aws_access_key_id
ENV AWS_SECRET_ACCESS_KEY aws_access_key_id
ENV AWS_REGION_NAME us-east-1
ENV AWS_BUCKET_NAME aws_bucket_name
ENV USER_NAME test
ENV PASSWORD password

# Run app.py when the container launches
CMD ["python", "basic-auth.py"]
