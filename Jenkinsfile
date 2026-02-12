pipeline {
    agent {
        docker {
            image 'docker:24-dind'
            args '--privileged'
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
                sh 'docker build -t mi-app:latest .'
            }
        }
    }
}
