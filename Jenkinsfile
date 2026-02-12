pipeline {
    agent {
        kubernetes {
            label 'python-pod'
            defaultContainer 'python'
            yaml """
apiVersion: v1
kind: Pod
spec:
  containers:
  - name: python
    image: python:3.11
    command:
    - cat
    tty: true
"""
        }
    }

    stages {
        stage('Test Pod') {
            steps {
                container('python') {
                    sh 'python --version'
                    sh 'echo Hola desde Minikube'
                }
            }
        }
    }
}
