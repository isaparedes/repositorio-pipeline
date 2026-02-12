pipeline {
    agent {
        kubernetes {
            label 'notes-pod'
            defaultContainer 'python'
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: jnlp
    image: jenkins/inbound-agent:4.13-4
    args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
  - name: python
    image: python:3.11
    command: ['cat']
    tty: true
  - name: docker
    image: docker:24.0.6
    command: ['cat']
    tty: true
"""
        }
    }

    stages {

        stage('Check Python') {
            steps {
                container('python') {
                    sh 'python --version'
                    sh 'echo Hola desde Minikube'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                container('docker') {
                    // Usa Docker dentro de Minikube
                    sh 'eval $(minikube docker-env)'
                    sh 'docker build -t notes-api:latest .'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                container('python') {
                    // Aplica tus manifests
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }
    }

    post {
        always {
            container('python') {
                sh 'echo Pipeline finalizado'
            }
        }
    }
}
