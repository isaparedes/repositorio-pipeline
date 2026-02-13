pipeline {
    agent {
        kubernetes {
            label 'test-agent'
            defaultContainer 'jnlp'
        }
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Build') {
            steps {
                sh 'echo "Compilando desde el repo en un pod efímero!"'
            }
        }
    }
}
