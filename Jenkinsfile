pipeline {
    agent {
        kubernetes {
            inheritFrom 'default-agent'
        }
    }
    stages {
        stage('Hello') {
            steps {
                sh 'echo "Hola desde un pod efímero en Kubernetes!"'
            }
        }
    }
}
