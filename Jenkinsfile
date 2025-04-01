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
                git branch: 'main', url: 'https://github.com/DanyaHDanny/tafordqe'
            }
        }
        stage('Install PostgreSQL Client') {
            steps {
                // Install PostgreSQL client
                sh 'apt-get update && apt-get install -y postgresql-client'
            }
        }
        stage('Execute SQL Commands') {
            steps {
                script {
                    // Execute the SQL commands in data.sql
                    sh """
                    PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -p ${DB_PORT} -U ${DB_USER} -d ${DB_NAME} -f data.sql
                    """
                }
            }
        }
    }
}