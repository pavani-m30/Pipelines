<<<<<<< HEAD
=======

pipeline {
    agent any

    stages {
        stage('Plan') {
            steps {
                echo '📋 Planning: checking dependencies, environment, and infra readiness...'
                sh 'python3 plan.py'
            }
        }

        stage('Code') {
            steps {
                echo '💻 Coding stage: linting and static analysis...'
                sh 'python3 -m flake8 src/'
            }
        }

        stage('Build') {
            steps {
                echo '🔨 Building the application...'
                sh 'python3 setup.py build'
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running unit and integration tests...'
                sh 'python3 -m unittest discover tests'
            }
        }

        stage('Package') {
            steps {
                echo '📦 Packaging artifacts...'
                sh 'python3 setup.py sdist bdist_wheel'
            }
        }

        stage('Release') {
            steps {
                echo '🚀 Preparing release candidate...'
                sh 'python3 release.py'
            }
        }

        stage('Deploy') {
            steps {
                echo '🌐 Deploying to target environment...'
                sh 'python3 deploy.py'
            }
        }

        stage('Monitor') {
            steps {
                echo '📊 Monitoring deployment health...'
                sh 'python3 monitor.py'
            }
        }
    }

    post {
        success {
            echo '✅ DevOps pipeline executed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Please check logs.'
        }
    }
}
>>>>>>> 753747ddd0afc88019a448d1ebab5b392c3e61ab
