pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/DanyaHDanny/tafordqe'
            }
        }
        stage('Set Up PostgreSQL Container') {
            steps {
                script {
                    // Run podman-compose to start PostgreSQL container
                    sh 'podman-compose -f podman-compose.yml up -d'
                }
            }
        }
        stage('Run SQL Script') {
            steps {
                script {
                    // Execute SQL script inside PostgreSQL container
                    sh '''
                    podman exec postgres_container psql -U admin -d my_database -f /data.sql
                    '''
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed!'
        }
    }
}