# FastAPI with Huey and Redis on Kubernetes

This repository demonstrates how to set up a FastAPI application with background task processing using Huey and Redis on Kubernetes.

## Prerequisites

- Docker
- Minikube
- kubectl

## Setup

1. Start Minikube:

```bash
minikube start

2. Build the Docker image:

```bash
docker build -t fastapi-app:latest .

3. Apply Kubernetes manifests:

```bash
kubectl apply -f redis-statefulset.yaml
kubectl apply -f fastapi-deployment.yaml
kubectl apply -f huey-consumer-job.yaml


4. Port forward the FastAPI service:

```bash
kubectl port-forward service/fastapi-service 8000:80


## Usage

1. Send a POST request to create a key-value pair:

```bash
curl -X 'POST' \
  'http://localhost:8000/create' \
  -H 'Content-Type: application/json' \
  -d '{
  "key": "welcome",
  "value": "india"
}'

2. Access the value by sending a GET request with the key:

```bash
curl -X 'GET' \
  'http://localhost:8000/welcome' \
  -H 'accept: application/json'


## Additional Notes

1. To monitor background task processing, check the logs of the huey-consumer job:

```bash
kubectl logs <huye-consumer-pod-name>

2. To access a Python shell in the FastAPI pod:

```bash
kubectl exec -it <fastapi-pod-name> -- /bin/sh
python



