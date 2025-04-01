pipeline {
    agent any
    environment {
        DB_HOST = 'postgres'  // PostgreSQL container name
        DB_PORT = '5432'      // PostgreSQL port inside the container
        DB_NAME = 'jenkins_db'
        DB_USER = 'jenkins'
        DB_PASSWORD = 'jenkins_password'
    }
    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/your-username/your-repo.git'
            }
        }
        stage('Install Python') {
            steps {
                // Install Python and pip
                sh 'apt-get update && apt-get install -y python3 python3-pip'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install psycopg2 for PostgreSQL
                sh 'pip3 install psycopg2'
            }
        }
        stage('Generate Data') {
            steps {
                script {
                    // Run the Python script to generate data
                    sh """
                    python3 generate_data.py
                    """
                }
            }
        }
    }
}