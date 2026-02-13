pipeline {
    agent {
        kubernetes {
            inheritFrom 'deploy-agent'
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
                    sh '/kaniko/executor --context=/home/jenkins/agent/workspace/${JOB_NAME}/app --dockerfile=/home/jenkins/agent/workspace/${JOB_NAME}/app/Dockerfile --destination=mi-app:latest --no-push'
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
