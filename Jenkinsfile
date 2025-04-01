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
        stage('Install Python') {
            steps {
                // Install Python and pip
                sh 'apt-get update'
                sh 'apt-get install -y python3 python3-pip'
                sh 'apt-get install python3.11-venv'
                //sh 'ln -s /usr/bin/python3 /usr/bin/python'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'apt-get install -y libpq-dev'
                    sh 'python -m venv venv'
                    sh '. venv/bin/activate && pip install psycopg2'
                }
            }
        }
        stage('Generate Data') {
            steps {
                script {
                    // Activate the virtual environment and run the Python script
                    sh '. venv/bin/activate && python main.py'
                }
            }
        }
    }
}


