pipeline {
    agent {
        kubernetes {
            label 'notes-pod'
            defaultContainer 'kubectl'
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: kubectl
    image: bitnami/kubectl:latest
    command:
    - cat
    tty: true
  - name: jnlp
    image: jenkins/inbound-agent:3355.v388858a_47b_33-3-jdk21
"""
        }
    }

    environment {
        DOCKER_IMAGE = "notes-api:latest"
    }

    stages {
        stage('Build Docker Image') {
            steps {
                container('kubectl') {
                    sh 'docker build -t $DOCKER_IMAGE ./app'
                }
            }
        }

        stage('Push Docker Image (Optional)') {
            steps {
                container('kubectl') {
                    // Solo si querés subir a algún registry
                    // sh 'docker tag $DOCKER_IMAGE myregistry/notes-api:latest'
                    // sh 'docker push myregistry/notes-api:latest'
                    echo 'Omitido push a registry por ahora'
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                container('kubectl') {
                    sh 'kubectl apply -f ./k8s/deployment.yaml'
                    sh 'kubectl apply -f ./k8s/service.yaml'
                }
            }
        }
    }

    post {
        always {
            echo "Build finalizada. El pod efímero se borrará automáticamente según la configuración de Kubernetes."
        }
    }
}
