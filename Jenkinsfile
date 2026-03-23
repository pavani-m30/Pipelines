pipeline {
    agent any

    environment {
        REPO_URL = 'https://github.com/pavani-m30/Pipelines.git'
        BRANCH_NAME = 'Main'
    }

    stages {
        stage('Plan') {
            steps {
                echo 'Planning pipeline execution...'
                echo "Repository: ${env.REPO_URL}"
                echo "Branch: ${env.BRANCH_NAME}"
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
                // Replace with your actual build command
                sh 'echo "Build step executed"'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Replace with your actual test command
                sh 'echo "Tests executed successfully"'
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying application...'
                // Replace with your actual deploy command
                sh 'echo "Deployment step executed"'
            }
        }

        stage('Monitor') {
            steps {
                echo 'Monitoring application health...'
                // Replace with your monitoring command
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

