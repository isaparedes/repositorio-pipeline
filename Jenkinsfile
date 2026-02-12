pipeline {
    agent any

    environment {
        IMAGE_NAME = "notes-api"
        IMAGE_TAG = "latest"
        KUBE_CONFIG = "C:\\Users\\isapa\\.kube\\config" // ruta de tu kubeconfig en Windows
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/isaparedes/repositorio-pipeline.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                // Usamos PowerShell para Windows
                powershell """
                # Configuramos el entorno de Docker de Minikube
                & minikube -p minikube docker-env --shell powershell | Invoke-Expression

                # Construimos la imagen
                docker build -t $env:IMAGE_NAME:$env:IMAGE_TAG .
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                powershell """
                # Reemplazamos la imagen en deployment.yaml
                (Get-Content deployment.yaml) -replace 'image: .*', "image: $env:IMAGE_NAME:$env:IMAGE_TAG" | Set-Content deployment.yaml

                # Aplicamos los YAML en el cluster
                kubectl --kubeconfig=$env:KUBE_CONFIG apply -f deployment.yaml
                kubectl --kubeconfig=$env:KUBE_CONFIG apply -f service.yaml
                """
            }
        }
    }

    post {
        success {
            echo "✅ Deploy a Kubernetes completado correctamente usando imagen local en Minikube (Windows)."
        }
        failure {
            echo "❌ Pipeline falló."
        }
    }
}
