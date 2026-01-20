pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/golan1202/pytest-demo'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t pytest-demo .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm -v $WORKSPACE:/app pytest-demo'
            }
            post {
                always {
                    junit 'report.xml'
                    archiveArtifacts artifacts: 'report.html', fingerprint: true
                }
            }
        }
    }
}
