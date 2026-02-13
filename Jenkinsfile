pipeline {
    agent {
        kubernetes {
            inheritFrom 'deploy-agent'   // usa tu Pod Template
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
                // Construye la imagen usando el Dockerfile en la carpeta app
                sh 'docker build -t mi-app:latest ./app'
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
