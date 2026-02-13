pipeline {
    agent {
        kubernetes {
            inheritFrom 'deploy-agent'
            defaultContainer 'jnlp'
            yaml """
            spec:
              containers:
              - name: kaniko
                image: gcr.io/kaniko-project/executor:debug
                command: ['sleep']
                args: ['infinity']
                tty: true
              - name: kubectl
                image: bitnami/kubectl:latest
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
        stage('Debug Kaniko') {
            steps {
                container('kaniko') {
                    sh 'pwd'
                    sh 'ls -l'
                    sh 'ls -l /home/jenkins/agent/workspace/${JOB_NAME}/app'
                }
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
