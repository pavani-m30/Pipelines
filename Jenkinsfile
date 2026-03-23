pipeline {
    agent any

    stages {
        stage('Plan') {
            steps {
                echo '📋 Planning: checking dependencies, environment, and infra readiness...'
                sh 'echo "Planing is done"'
            }
        }

        stage('Code') {
            steps {
                echo '💻 Coding stage: linting and static analysis...'
                sh 'echo "code is done"'
            }
        }

        stage('Build') {
            steps {
                echo '🔨 Building the application...'
                sh 'echo "it is in build process"'
       }
        }

        stage('Test') {
            steps {
                echo '🧪 Running unit and integration tests...'
                sh 'echo "test is done"'
            }
        }

        stage('Package') {
            steps {
                echo '📦 Packaging artifacts...'
                sh 'echo "package is being built"'
            }
        }

        stage('Release') {
            steps {
                echo '🚀 Preparing release candidate...'
                sh 'echo "it is in building phase"'
            }
        }

        stage('Deploy') {
            steps {
                echo '🌐 Deploying to target environment...'
                sh 'echo "it is ready to deploy"'
            }
        }

        stage('Monitor') {
            steps {
                echo '📊 Monitoring deployment health...'
                sh 'echo "it is monitoring"'
            }
        }    }

    post {
        success {
            echo '✅ DevOps pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}


