pipeline {
    agent any
    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/DanyaHDanny/tafordqe'
            }
        }
        stage('Create PostgreSQL Container') {
            steps {
                script {
                    // Run Podman Compose on the Windows host to create the PostgreSQL container
                    bat '''
                    podman-compose -f podman-compose.yml up -d
                    '''
                }
            }
        }
        stage('Run SQL Script') {
            steps {
                script {
                    // Wait for PostgreSQL container to be ready and execute the SQL script
                    bat '''
                    timeout /t 10
                    podman exec -i postgres_container psql -U admin -d my_database < data.sql
                    '''
                }
            }
        }
    }
}