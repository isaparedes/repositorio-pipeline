pipeline {
    agent any

    environment {
        IMAGE_NAME = "notes-api"
        IMAGE_TAG = "latest"
        KUBE_CONFIG = "/var/jenkins_home/.kube/config" // ruta al kubeconfig en Linux
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/isaparedes/repositorio-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh """
                # Configuramos Docker para usar el Docker de Minikube
                eval \$(minikube -p minikube docker-env)

                # Construimos la imagen
                docker build -t $IMAGE_NAME:$IMAGE_TAG .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh """
                # Reemplazamos la imagen en deployment.yaml
                sed -i 's|image: .*|image: $IMAGE_NAME:$IMAGE_TAG|' deployment.yaml

                # Aplicamos los YAML en el cluster
                kubectl --kubeconfig=$KUBE_CONFIG apply -f deployment.yaml
                kubectl --kubeconfig=$KUBE_CONFIG apply -f service.yaml
                """
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
