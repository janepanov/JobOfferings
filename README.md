# JobOfferings

## Overview
JobOfferings is a FastAPI application that manages job offerings with PostgreSQL as the database. This project demonstrates containerization with Docker, orchestration with Kubernetes, and a CI/CD pipeline using GitHub Actions.

## Setup Instructions

### Clone the Repository
```bash
git clone https://github.com/janepanov/JobOfferings.git
cd JobOfferings
```

### Start Minikube
```bash
minikube start
minikube status
minikube addons enable ingress
minikube addons enable ingress-dns
```

### Build and Start Docker Containers
_Ensure Docker Desktop is active._
```bash
docker compose build
docker compose up -d

Alternative:
docker compose up -d --build
```

### Deploy to Kubernetes
```bash
cd kubernetes

kubectl apply -f namespace.yaml
kubectl apply -f secret.yaml
kubectl apply -f configmap.yaml
kubectl apply -f statefulset.yaml
kubectl apply -f postgres-service.yaml
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f ingress.yaml

kubectl config set-context --current --namespace=workerhub
```

### Check Deployment Status
```bash
docker ps -a

kubectl get pods
kubectl get deployments
kubectl get services
kubectl get ingress
```

### Port Forward to Access the Application
```bash
kubectl port-forward -n workerhub <app-pod-name> 8888:80 &
```

**Access the website in your browser:**
```bash
Application: localhost:8888
API Documentation: localhost:8888/docs
```

### Populate the Database
```bash
kubectl exec -it postgres-0 -n workerhub -- psql -U postgres -d jobofferings
```

**Run the following SQL to insert data:**

```bash
INSERT INTO job_offerings (title, company, location, description, salary, remote) VALUES
    ('DevOps Engineer', 'Tech Solutions Inc.', 'Remote', 'Implementing CI/CD pipelines using Jenkins and Kubernetes', 120000.0, true),
    ('Software Engineer', 'Web Apps Co.', 'San Francisco', 'Developing scalable web applications using Python and Django', 130000.0, false),
    ('Cloud Architect', 'Cloud Services Ltd.', 'Seattle', 'Designing and implementing cloud solutions on AWS', 140000.0, true),
    ('Site Reliability Engineer', 'Web Apps Co.', 'New York', 'Ensuring high availability and performance of web applications', 125000.0, false),
    ('Security Analyst', 'Secure Solutions', 'Boston', 'Performing vulnerability assessments and implementing security measures', 110000.0, true);
```

## Access Job Offerings
_Visit localhost:8888/job-offerings to see the data as JSON objects._

# Troubleshooting
If you have already dockerized the app before, using docker compose down and trying to docker compose up again might result in an error that the table job_offerings already exists. This is because the database pod is persistent and retains the data despite any "failures." The app tries to recreate the database schema on every failure.

To avoid this problem, you can use docker compose stop or go inside the database pod, enter the database with psql -U postgres jobofferings, and run the following commands:

```bash
DROP TABLE IF EXISTS job_offerings CASCADE;
DROP SEQUENCE IF EXISTS job_offerings_id_seq;
```

Afterwards, restart the container, and everything should work as intended.`
