# Exercise 3: Scaling Flask App on a Single Node Using ReplicaSets

## Real-Life Use Case: E-commerce Flash Sale

During an e-commerce flash sale, traffic can increase suddenly. Kubernetes ReplicaSets help maintain the desired number of application Pods by creating additional Pods when scaling up and replacing deleted Pods.

## Objective
- Understand Kubernetes Pods and ReplicaSets.
- Deploy a Flask application.
- Scale from 3 replicas to 5 replicas.
- Observe Pod distribution across a single node.
- Verify automatic Pod replacement.

## Technologies Used
- Python and Flask
- Docker
- Kubernetes
- Minikube
- kubectl
- GitHub

## Application Endpoints
- `/` — Displays a welcome message and the serving Pod name.
- `/buy?user=123` — Simulates a purchase and identifies the serving Pod.
- `/health` — Returns the application's health status.

## Implementation Steps
1. Created the Flask application in `app.py`.
2. Created a Dockerfile to package the application.
3. Started a single-node Minikube cluster.
4. Built the `flashsale:1.0` Docker image.
5. Created a ReplicaSet and Service configuration.
6. Applied the configuration using `kubectl apply`.
7. Verified the initial three Pods.
8. Scaled the ReplicaSet to five replicas.
9. Verified Pod distribution using `kubectl get pods -o wide`.
10. Deleted one Pod and verified automatic replacement.

## Important Commands

Start Minikube:
```bash
minikube start --nodes=1
```

Build the image:
```bash
minikube image build -t flashsale:1.0 .
```

Apply the configuration:
```bash
kubectl apply -f flashsale-replicaset.yaml
```

Check Pods and ReplicaSets:
```bash
kubectl get pods
kubectl get rs
kubectl get pods -o wide
```

Scale to five replicas:
```bash
kubectl scale rs flashsale-rs --replicas=5
```

Delete a Pod:
```bash
kubectl delete pod <actual-pod-name>
```

Access the Service:
```bash
minikube service flashsale-svc --url
```

## Observations and Results
- Initially, three replicas were configured.
- Scaling to five replicas caused Kubernetes to create two additional Pods.
- All five Pods ran on the single Minikube node.
- Deleting a Pod caused the ReplicaSet to create a replacement.
- The Service provided a stable endpoint for accessing the application.

## Questions and Answers

**1. What was the initial number of replicas?**

Three replicas.

**2. How many Pods were running initially?**

Three Pods, once all became ready.

**3. What happened when scaling to five replicas?**

Kubernetes created two additional Pods.

**4. What happened when one Pod was deleted?**

The ReplicaSet created a replacement Pod to maintain five replicas.

**5. How does Kubernetes maintain the desired number of replicas?**

It compares the actual number of matching Pods with the desired number and creates or removes Pods as needed.

**6. How many nodes were running?**

One Minikube node.

**7. Where were the five Pods running?**

All five Pods were scheduled on the single Minikube node.

## Conclusion

This exercise demonstrated how Kubernetes ReplicaSets manage the desired number of Pods, support scaling, and replace deleted Pods automatically. The Kubernetes Service provided a stable endpoint for accessing the Flask application.

## Evidence
Add screenshots of your actual command outputs showing:
1. `kubectl get nodes`
2. Three initial Pods.
3. Five running Pods.
4. All five Pods on one node.
5. Automatic Pod replacement.
6. Successful application endpoint responses.
