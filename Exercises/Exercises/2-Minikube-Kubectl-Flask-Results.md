# Exercise 2: Minikube, Kubectl and Flask

## Objective
Deploy a Flask application on a local Kubernetes cluster using Minikube and Docker.

## Environment
- Operating System: macOS
- Processor: Apple M2
- Container Runtime: Docker Desktop
- Kubernetes Tools: kubectl and Minikube
- Application: Python Flask

## Project Files
- `app.py` — Flask application
- `Dockerfile` — Instructions to build the application container
- `deployment.yaml` — Kubernetes deployment configuration
- `requirements.txt` — Python dependencies

## Steps Performed
1. Created the Flask application.
2. Prepared the Dockerfile and Python dependencies.
3. Created the Kubernetes deployment configuration.
4. Started the local Kubernetes environment using Minikube.
5. Deployed the Flask application to Kubernetes.
6. Checked the Kubernetes pods and exposed the application through a Kubernetes Service.

## Verification
The Terminal showed the `flask-k8s` and `nginx` pods in the Running state. A Kubernetes Service was exposed for the Flask deployment.

## Result
The Flask Kubernetes deployment files were created and uploaded to the DevOps-Lab GitHub repository.

