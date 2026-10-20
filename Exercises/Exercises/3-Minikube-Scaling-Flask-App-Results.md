# Exercise 3: Scaling Flask App on a Single Node Using ReplicaSets

## Real-Life Use Case: E-commerce Flash Sale

During an e-commerce flash sale, traffic can increase suddenly. Kubernetes ReplicaSets maintain the desired number of application Pods by creating additional Pods when scaling up and replacing deleted Pods.

## Objective
- Understand Kubernetes Pods and ReplicaSets.
- Deploy a Flask application.
- Scale the ReplicaSet from 3 to 5 replicas.
- Observe Pod distribution across one node.
- Verify automatic Pod replacement.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl

## Application Endpoints
- `/` — Displays a welcome message and the serving Pod name.
- `/buy?user=123` — Simulates a purchase and identifies the serving Pod.
- `/health` — Returns the application's health status.

## Dockerfile

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask gunicorn
EXPOSE 5000
CMD ["gunicorn", "-b", "0.0.0.0:5000", "app:app", "--workers", "1", "--threads", "2"]
```

## Minikube Setup

```bash
minikube start --nodes=1
kubectl get nodes
```

Build the image:

```bash
minikube image build -t flashsale:1.0 .
```

## ReplicaSet Configuration

Create `flashsale-replicaset.yaml` with a ReplicaSet named `flashsale-rs` configured for 3 replicas and a ClusterIP Service named `flashsale-svc`. The container image is `flashsale:1.0`, with port 5000 and `/health` readiness and liveness probes.

Apply the configuration:

```bash
kubectl apply -f flashsale-replicaset.yaml
kubectl get rs
kubectl get pods
```

## Scaling from 3 to 5 Replicas

```bash
kubectl scale rs flashsale-rs --replicas=5
kubectl get rs
kubectl get pods
kubectl get pods -o wide
```

Kubernetes creates two additional Pods to reach five replicas.

## Automatic Pod Replacement

Delete one of the actual Pod names:

```bash
kubectl delete pod <actual-pod-name>
```

Verify replacement:

```bash
kubectl get pods
kubectl get rs
```

The ReplicaSet creates a replacement Pod to maintain five replicas.

## Testing the Application

Get the Service URL:

```bash
minikube service flashsale-svc --url
```

Test the homepage, purchase, and health endpoints using the returned URL:

```bash
curl http://<service-url>/
curl "http://<service-url>/buy?user=123"
curl http://<service-url>/health
```

Replace `<service-url>` with the actual host and port returned by Minikube.

## Useful Inspection Commands

```bash
kubectl describe rs flashsale-rs
kubectl describe pod <actual-pod-name>
kubectl logs <actual-pod-name>
kubectl describe svc flashsale-svc
```

## Observations
- Initially, 3 replicas were configured.
- Scaling created 2 additional Pods.
- All 5 Pods ran on the single Minikube node.
- Deleting one Pod caused the ReplicaSet to create a replacement.
- The Service provided a stable endpoint for accessing the application.

## Conclusion

This exercise demonstrated how Kubernetes ReplicaSets maintain the desired number of Pods, support scaling, and replace deleted Pods automatically. The Service provided a stable endpoint for accessing the Flask application.

## Evidence
Add screenshots of your actual outputs showing:
1. The Minikube node.
2. Three initial Pods.
3. Five running Pods.
4. Five Pods distributed on one node.
5. Automatic Pod replacement.
6. Successful application endpoint responses.
