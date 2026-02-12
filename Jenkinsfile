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
    image: jenkins/inbound-agent:latest
    args: ['\$(JENKINS_SECRET)', '\$(JENKINS_NAME)']
  - name: python
    image: python:3.11
    command: ['cat']
    tty: true
"""
        }
    }

    environment {
        DOCKER_ENV = '' // se llenará en el stage
    }

    stages {

        stage('Test Pod') {
            steps {
                container('python') {
                    sh 'python --version'
                    sh 'echo Pod funcionando en Minikube'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                container('python') {
                    // Usamos el Docker de Minikube
                    sh 'eval $(minikube docker-env)'
                    sh 'docker build -t notes-api:latest .'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                container('python') {
                    sh 'kubectl apply -f deployment.yaml'
                    sh 'kubectl apply -f service.yaml'
                }
            }
        }

    }

    post {
        always {
            container('python') {
                sh 'echo Pipeline finalizada'
            }
        }
    }
}
