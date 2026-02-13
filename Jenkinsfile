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

    stages {
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
            echo "Pipeline finalizado. El pod efímero de Jenkins se eliminará automáticamente."
        }
    }
}
