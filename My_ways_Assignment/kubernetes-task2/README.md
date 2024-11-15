Resource Monitoring Application - Documentation
Overview
This application monitors various system resources including CPU, memory, disk, and network usage. It provides an API endpoint (/health) that returns the current resource utilization in JSON format.

The application is built using Python and the Flask web framework. The system is containerized using Docker and can be deployed on Kubernetes using Helm.

Features
Monitors CPU, memory, disk, and network resources.
Provides real-time resource utilization through a REST API.
Exposes the /health endpoint to fetch the resource data in JSON format.
Requirements
Python 3.x: The application is built using Python, version 3.12.3 or later.
Docker: To containerize the application.
Kubernetes: To orchestrate and deploy the application.
Helm: For managing Kubernetes deployments.
Prerequisites
Before deploying or running the application, ensure the following tools are installed:

Docker
Minikube (or Kubernetes cluster)
Helm
psutil (Python package for resource monitoring)
Installation

1. Clone the Repository
   Clone the repository containing the application code and Helm charts.

bash
Copy code
git clone <repository_url>
cd <project_directory> 2. Build the Docker Image
In the root directory of the project, build the Docker image:

bash
Copy code
docker build -t kubernetes-task2:latest . 3. Run Locally (Optional)
To test the application locally, run the Docker container using the following command:

bash
Copy code
docker run -p 5001:5000 kubernetes-task2
You can access the application by visiting http://localhost:5001/health.

4. Create Helm Chart for Kubernetes Deployment
   If you're deploying the application in Kubernetes, you need to configure Helm charts. Ensure the following structure is in your project directory:

Copy code
.
├── app.py
├── Dockerfile
├── requirements.txt
├── kubernetes_task2_chart/
│ ├── charts/
│ ├── templates/
│ └── values.yaml
├── helm_chart_values.yaml
└── README.md
Note: Make sure you have the correct values in values.yaml for the Kubernetes deployment.

5. Deploy Application on Kubernetes Using Helm
   Once you have configured the Helm charts, you can deploy the application to your Kubernetes cluster:

bash
Copy code
helm install kubernetes-task2 ./kubernetes_task2_chart
You can verify the deployment with:

bash
Copy code
kubectl get pods 6. Accessing the Application
Expose the application on a local port using a NodePort or Ingress (based on your setup). If using a NodePort, you can access the app via the node's IP and port.

To expose the application as a NodePort service, modify service.yaml in the Helm chart:

yaml
Copy code
apiVersion: v1
kind: Service
metadata:
name: kubernetes-task2-service
spec:
type: NodePort
selector:
app: kubernetes-task2
ports: - protocol: TCP
port: 5000
targetPort: 5000
nodePort: 30001
Now, you can access the application by visiting:

arduino
Copy code
http://<node_ip>:30001/health
Monitoring
The application is designed to monitor system resources using the psutil library. The /health endpoint returns a JSON response containing data on:

CPU usage (overall and per core)
Memory usage (total, available, used, percent)
Disk usage (total, used, free, percent)
Disk I/O (read and write bytes)
Network I/O (sent and received bytes)
Example Response:
json
Copy code
{
"cpu": {
"cpu_percent": 45.5,
"cpu_per_core": [25.3, 30.2, 15.7],
"cpu_count": 4
},
"memory": {
"memory_total": 8589934592,
"memory_available": 4294967296,
"memory_used": 3435973836,
"memory_percent": 50.0
},
"disk": {
"disk_total": 21474836480,
"disk_used": 10737418240,
"disk_free": 10737418240,
"disk_percent": 50.0
},
"disk_io": {
"disk_read": 1024,
"disk_write": 2048
},
"network": {
"net_sent": 1000000,
"net_recv": 500000
}
}
Cleanup
To clean up the Kubernetes deployment and remove the application, run:

bash
Copy code
helm uninstall kubernetes-task2
To remove the Docker image locally:

bash
Copy code
docker rmi kubernetes-task2:latest
Troubleshooting
Common Issues:
Port Binding Error: If you're running the container and encountering port binding errors, ensure that the specified port is not being used by another process. You can use netstat or lsof to check which process is using the port.

Minikube Issues: If you're using Minikube and face issues loading images, ensure that Minikube is running and that your Docker daemon is properly configured to work with Minikube.

Helm Installation Failures: Make sure that Helm is correctly installed and configured. Also, ensure that you are providing the correct release name during the installation.

Conclusion
This application provides basic resource monitoring functionality with a Flask-based API. It can be run locally via Docker or deployed to a Kubernetes cluster using Helm for scalability and orchestration.
