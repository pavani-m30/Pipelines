pipeline {
    agent any

    tools {
        maven 'Maven'   // Make sure Maven is installed in Jenkins
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/pavani-m30/apnacollege.git'
            }
        }

        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }

        stage('SonarQube Analysis') {
            environment {
                SONARQUBE = credentials('sonar-token-id') // Jenkins credential ID for your SonarQube token
            }
            steps {
                withSonarQubeEnv('SonarQube') {
                    sh '''
                        sonar-scanner \
                          -Dsonar.projectKey=pipeline \
                          -Dsonar.sources=. \
                          -Dsonar.java.binaries=target/classes \
                          -Dsonar.host.url=http://localhost:9000 \
                          -Dsonar.login=$SONARQUBE
                    '''
                }
            }
        }
    }
}
