# Application Deployment on Kubernetes Using Helm

## Part 2: Application Deployment on Kubernetes Using Helm

This documentation provides a step-by-step guide to deploying an application on a Kubernetes cluster using Helm. It also outlines how to implement basic monitoring for the deployed application.

---

## Objectives

1. Deploy an application of your choice on a Kubernetes cluster using Helm charts.
2. Implement basic monitoring for the application.
3. Expose the application locally via the cluster.
4. Ensure the application is accessible via Kubernetes services.

---

## Functional Requirements

### Kubernetes Setup

1. **Kubernetes Cluster**:
    - Use Minikube, Kind, or any local Kubernetes environment for deployment.
    - Ensure Kubernetes is running locally. You can start Minikube with the following command:
    
    ```bash
    minikube start
    ```

2. **Helm Setup**:
    - Install Helm, the Kubernetes package manager.
    - Ensure Helm is installed by running:
    
    ```bash
    helm version
    ```

3. **Helm Chart Organization**:
    - Organize your Helm charts for easy management and reusability.

### Application Deployment

1. **Create a Flask Application** (or any preferred application):
    - The app monitors system resources using the `psutil` library.
    - You can use the following basic `app.py` as an example:

    ```python
    from flask import Flask, jsonify
    import psutil

    app = Flask(__name__)

    @app.route('/health')
    def health():
        # System health metrics logic
        ...
    
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=5000)
    ```

2. **Dockerize the Application**:
    - Create a `Dockerfile` for your application.
    
    ```dockerfile
    FROM python:3.12-slim

    WORKDIR /app

    RUN apt-get update && apt-get install -y gcc python3-dev

    COPY requirements.txt requirements.txt
    RUN pip install --no-cache-dir -r requirements.txt

    COPY . .

    EXPOSE 5000

    CMD ["python", "app.py"]
    ```

3. **Build the Docker Image**:
    - Build the Docker image locally.
    
    ```bash
    docker build -t kubernetes-task2 .
    ```

4. **Load the Image into Minikube**:
    - Minikube has its own Docker daemon, so to use the image inside Minikube, you need to load the image.
    
    ```bash
    minikube image load kubernetes-task2:latest
    ```

5. **Create a Helm Chart for Kubernetes Deployment**:
    - Structure the Helm chart with the following folder structure:
    
    ```bash
    kubernetes_task2_chart/
    ├── charts/
    ├── templates/
    │   ├── deployment.yaml
    │   ├── service.yaml
    │   └── ingress.yaml
    ├── values.yaml
    └── Chart.yaml
    ```

6. **Helm Chart Templates**:

    - **deployment.yaml**:
    
    ```yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: kubernetes-task2
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: kubernetes-task2
      template:
        metadata:
          labels:
            app: kubernetes-task2
        spec:
          containers:
            - name: kubernetes-task2
              image: "kubernetes-task2:latest"
              ports:
                - containerPort: 5000
    ```

    - **service.yaml**:
    
    ```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: kubernetes-task2
    spec:
      selector:
        app: kubernetes-task2
      ports:
        - protocol: TCP
          port: 80
          targetPort: 5000
      type: NodePort
    ```

7. **Deploy the Application with Helm**:
    - Run the following Helm command to deploy the application:
    
    ```bash
    helm install kubernetes-task2 ./kubernetes_task2_chart
    ```

8. **Expose the Application**:
    - The application can be accessed locally by exposing it via a `NodePort` service (configured in the `service.yaml` file).

    ```bash
    kubectl get svc
    ```

    Look for the `NodePort` value under `PORT(S)` and use it to access the application locally.

### Monitoring

1. **Prometheus Setup**:
    - Install Prometheus for monitoring the application.
    
    ```bash
    helm install prometheus prometheus-community/prometheus
    ```

2. **Grafana Setup**:
    - Install Grafana to visualize the metrics.
    
    ```bash
    helm install grafana grafana/grafana
    ```

3. **Configure Prometheus Scraping**:
    - In the `values.yaml` file of your Helm chart, add Prometheus scraping configuration for your Flask application.
    
    ```yaml
    prometheus:
      enabled: true
      serviceMonitor:
        enabled: true
        namespace: default
        selector:
          matchLabels:
            app: kubernetes-task2
    ```

4. **Access Grafana Dashboard**:
    - Once Grafana is installed, you can access it through the Kubernetes service:
    
    ```bash
    kubectl port-forward svc/grafana 3000:80
    ```

    Open your browser and go to `http://localhost:3000` to view the Grafana dashboard. Use the default credentials (`admin/admin`) to log in.

---

## Non-Functional Requirements

### Performance

- Ensure that the application and infrastructure are optimized for performance and scaling.
  
### Security

1. **Secret Management**:
    - Securely manage secrets such as API keys and database credentials using tools like AWS Secrets Manager or Kubernetes Secrets.

2. **Access Control**:
    - Implement proper access control for both Kubernetes and Helm to ensure the security of the deployment.

### Logging & Monitoring

1. **Enable Application Logs**:
    - Ensure that your application is logging useful information for debugging and monitoring.

2. **Set Up Monitoring Tools**:
    - Use Prometheus and Grafana (or equivalent tools) to monitor application health and resource usage.

---

## Technical Requirements

### Technology Stack

1. **Backend**: Python (Flask)
2. **Containerization**: Docker
3. **Orchestration**: Kubernetes (Minikube)
4. **Package Management**: Helm
5. **Monitoring**: Prometheus, Grafana

### Deployment

- The application must be accessible locally via Kubernetes. You can test the application after deploying using the NodePort.

---
