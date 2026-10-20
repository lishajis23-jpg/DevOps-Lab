# Kubernetes Getting Started — Exercise Results

## Objective
Deploy an Nginx container on a local Kubernetes cluster using Minikube and access it through a Kubernetes Service.

## Environment
- Operating System: macOS Tahoe 26.3
- Processor: Apple M2 (Apple silicon)
- Container runtime: Docker Desktop
- Kubernetes tools: kubectl and Minikube
- Minikube driver: Docker

## Steps Performed

### 1. Start the Kubernetes cluster
```bash
minikube start --driver=docker
```

### 2. Verify the cluster
```bash
kubectl get nodes
```
Result: The `minikube` node reached `Ready` status.

### 3. Create the Nginx Pod
```bash
kubectl run nginx --image=nginx
```

### 4. Verify the Pod
```bash
kubectl get pods
```
Result: The `nginx` Pod reached `Running` status with `1/1` containers ready.

### 5. Expose Nginx as a Service
```bash
kubectl expose pod nginx --type=NodePort --port=80
```

### 6. Verify the Service
```bash
kubectl get services
```

### 7. Access Nginx
```bash
minikube service nginx
```
Result: The browser displayed the **Welcome to nginx!** page.

## Conclusion
Successfully created a local Kubernetes cluster, deployed an Nginx Pod, exposed it through a NodePort Service, and verified that the application was accessible in a browser.
