pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                checkout scm
            }
        }

        stage('Build image') {
            steps {
                sh 'docker build -t notes-api .'
            }
        }

        stage('Run container') {
            steps {
                sh '''
                docker rm -f notes-api || true
                docker run -d \
                  -p 5001:5001 \
                  -v notes_data:/data \
                  --name notes-api \
                  notes-api
                '''
            }
        }
    }
}