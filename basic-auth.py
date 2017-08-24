#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import request, Response, Flask
from functools import wraps
import boto3
import os

app = Flask(__name__)
s3 = boto3.resource('s3',
  region_name           = os.environ.get('AWS_REGION_NAME'),
  aws_access_key_id     = os.environ.get('AWS_ACCESS_KEY_ID'),
  aws_secret_access_key = os.environ.get('AWS_SECRET_ACCESS_KEY'))
bucket = s3.Bucket(os.environ.get('AWS_BUCKET_NAME'))

def check_auth(username, password):
  """This function is called to check if a username /
  password combination is valid.  """
  return username == os.getenv('USER_NAME', 'admin') and password == os.getenv('PASSWORD', 'admin123')

def authenticate():
  """Sends a 401 response that enables basic auth"""
  return Response(
  'Could not verify your access level for that URL.\n'
  'You have to login with proper credentials', 401,
  {'WWW-Authenticate': 'Basic realm="Login Required"'})

def requires_auth(f):
  @wraps(f)
  def decorated(*args, **kwargs):
    auth = request.authorization
    if not auth or not check_auth(auth.username, auth.password):
      return authenticate()
    return f(*args, **kwargs)
  return decorated

@app.route("/test")
@requires_auth
def test():
  return "TEST OK"

@app.route("/<path:path>", methods=['PUT'])
@requires_auth
def put_object_to_s3_repo(path):
  data = request.data
  bucket.put_object(Key=path, Body=data)
  return "ok"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
