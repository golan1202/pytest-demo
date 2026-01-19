pipeline {
    agent any

    triggers {
        cron('H 2 * * *')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Image') {
            steps {
                sh 'docker build -t pytest-demo .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm -v $WORKSPACE:/app pytest-demo'
            }
        }
    }

    post {
        always {
            junit 'report.xml'
            archiveArtifacts artifacts: 'report.html, pytest.log, htmlcov/**'
        }
    }
}
