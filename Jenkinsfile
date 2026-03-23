pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/pavani-m30/Pipelines.git'
        BRANCH_NAME = 'main'
    }

    stages {
        stage('Plan') {
            steps {
                echo 'Planning pipeline execution...'
                echo "Repository: ${env.REPO_URL}"
                echo "Branch: ${env.BRANCH_NAME}"
                
                // Run your Python file here
                sh 'python3 prime.py'
                sh 'python3 factorial.py'
            }
        }
        
        stage('Checkout') {
            steps {
                echo 'Checking out repository...'
                git branch: "${env.BRANCH_NAME}", url: "${env.REPO_URL}"
            }
        }

        stage('Build') {
            steps {
                echo 'Running build commands...'
                sh 'echo "Build step executed"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                sh 'echo "Tests executed successfully"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                sh 'echo "Deployment step executed"'
            }
        }

        stage('Monitor') {
            steps {
                echo 'Monitoring application health...'
                sh 'echo "Monitoring step executed"'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check logs.'
        }
    }
}
