pipeline {
    agent {
        kubernetes {
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: kaniko
    image: gcr.io/kaniko-project/executor:debug
    command:
    - /kaniko/executor
    args:
    - --context=/home/jenkins/agent/workspace/pipeline20001/app
    - --dockerfile=/home/jenkins/agent/workspace/pipeline20001/app/Dockerfile
    - --destination=mi-app:latest
    - --no-push
    tty: true
  - name: kubectl
    image: bitnami/kubectl:debug
    command: ['sleep']
    args: ['infinity']
    tty: true
"""
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build Docker Image') {
            steps {
                container('kaniko') {
                    echo "Kaniko ejecutando build directamente"
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                container('kubectl') {
                    sh 'kubectl apply -f k8s/deployment.yaml'
                    sh 'kubectl apply -f k8s/service.yaml'
                }
            }
        }
    }
}
