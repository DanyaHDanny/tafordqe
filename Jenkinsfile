pipeline {
    agent any

    environment {
        DB_HOST = 'localhost'
        DB_PORT = '5434'  // Updated port
        DB_USER = 'admin'
        DB_PASSWORD = 'admin123'
        DB_NAME = 'postgres'
    }

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the repository containing Podman setup and SQL files
                git branch: 'main', url: 'https://github.com/DanyaHDanny/tafordqe'
            }
        }

        stage('Build Podman Container') {
            steps {
                // Start PostgreSQL container
                sh '''
                podman-compose up -d
                '''
            }
        }

        stage('Feed Data into PostgreSQL') {
            steps {
                // Run the script to feed data
                sh '''
                chmod +x feed_data.sh
                ./feed_data.sh
                '''
            }
        }
    }

    post {
        always {
            // Stop and remove Podman containers
            sh '''
            podman-compose down
            '''
        }
    }
}