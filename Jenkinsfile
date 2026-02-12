pipeline {
    agent any

    environment {
        IMAGE_NAME = "notes-api"                 // nombre de la imagen local
        IMAGE_TAG = "latest"
        KUBE_CONFIG = "/var/jenkins_home/.kube/config" // Jenkins necesita acceso a kubectl
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/isaparedes/repositorio-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Esto asegura que la imagen quede en el Docker de Minikube
                sh """
                eval \$(minikube -p minikube docker-env)
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                // Actualiza deployment.yaml con la imagen local
                sh "sed -i 's|image: .*|image: $IMAGE_NAME:$IMAGE_TAG|' deployment.yaml"

                // Aplica los YAML en el cluster
                sh "kubectl --kubeconfig=$KUBE_CONFIG apply -f deployment.yaml"
                sh "kubectl --kubeconfig=$KUBE_CONFIG apply -f service.yaml"
            }
        }
    }

    post {
        success {
            echo "✅ Deploy a Kubernetes completado correctamente usando imagen local en Minikube."
        }
        failure {
            echo "❌ Pipeline falló."
        }
    }
}
