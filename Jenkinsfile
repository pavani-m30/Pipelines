pipeline {
    agent any

    stages {
        stage('Create Directory and File') {
            steps {
                script {
                    def dirName = "my_directory"
                    def fileName = "${dirName}/hello.txt"

                    // Create directory
                    sh "mkdir -p ${dirName}"

                    // Check if directory exists
                    if (fileExists(dirName)) {
                        echo "✅ Directory '${dirName}' created successfully!"

                        // Create file with timestamp
                        sh "echo \"File created at $(date)\" > ${fileName}"

                        // Show directory contents
                        sh "ls -l ${dirName}"

                        // Show file contents
                        sh "cat ${fileName}"
                    } else {
                        error "❌ Directory '${dirName}' was not created!"
                    }
                }
            }
        }
    }

    post {
        success {
            echo '🎉 Pipeline executed successfully!'
        }
        failure {
            echo '⚠️ Pipeline failed. Please check logs.'
        }
    }
}
