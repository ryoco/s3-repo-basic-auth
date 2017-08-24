
# s3-repo-basic-auth

Just upload the file to s3 using basic authentication

## Getting Started

* Using docker example

```
cd s3-repo-basic-auth
docker build -t image-name .
docker run -e AWS_ACCESS_KEY_ID="id" -e AWS_SECRET_ACCESS_KEY="key" -e AWS_BUCKET_NAME="bucket-name" -e AWS_REGION_NAME="ap-northeast-1" -d -p 8088:5000 image-name
```

## License

MIT
