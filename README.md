# Lambda to write to Parquet

Simple PoC to implement lightweight write to Parquet on AWS Lambda.

Since there is no library that can write Parquets using pure python, it is not as straightforward as uploading a zip file to Lambda.
These zip files contain pyx and pxd files (C ports) which if not given the proper environment, fails to run.

Therefore, this project uses Docker.

## Building Docker Image and Pushing to ECR

Create a repository in ECR and get it's URL. For example: `123456789012.dkr.ecr.eu-west-2.amazonaws.com/pyarrow_lambda`

```bash
# Log into ECR
aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin 123456789012.dkr.ecr.eu-west-2.amazonaws.com/pyarrow_lambda

# Build Image
$ docker build -t pyarrow_lambda .

# Tag image
docker tag pyarrow_lambda:latest 123456789012.dkr.ecr.eu-west-2.amazonaws.com/pyarrow_lambda:latest

# Push Image
docker push 123456789012.dkr.ecr.eu-west-2.amazonaws.com/pyarrow_lambda:latest
```

## Deploying on AWS Console

1. Create a new Lambda function

2. Select "Container Image" as build from option.

3. Give it a relevant name.

4. Use browse images to find the image you pushed above.

5. Select x86_64 architecture.

6. Perform additional configuration as necessary.

7. Create Function.

8. Write a test and execute.

## Running Locally

You can start the container locally and send it events to test. If you want to see the output file created, you can mount it as a volume.

```bash
$ docker run pyarrow_lambda

# In a separate terminal
$ curl -X POST "http://localhost:9000/2015-03-31/functions/function/invocations" -d '{"key": "value"}'

```
