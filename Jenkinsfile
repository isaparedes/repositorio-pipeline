pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                sh 'echo "Building the application..."'
                // Add your build commands here (e.g., mvn clean install)
            }
        }
        stage('Test') {
            steps {
                sh 'echo "Running tests..."'
                // Add your test commands here
            }
        }
        stage('Deploy') {
            steps {
                sh 'echo "Deploying the application..."'
                // Add your deploy commands here
            }
        }
    }
}
