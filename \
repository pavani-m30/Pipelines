pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Compiling Java program...'
                sh 'javac SumExample.java'
            }
        }

        stage('Run') {
            steps {
                echo 'Running Java program...'
                sh 'java SumExample'
            }
        }
    }
}

