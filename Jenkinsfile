pipeline {
    agent any
    environment {
        PODMAN_SOCKET = '/run/user/0/podman/podman.sock' // Path to Podman socket
        PODMAN_API_URL = 'http://d/v1.0.0/libpod'       // Podman REST API base URL
    }
    stages {
        stage('Clone Repository') {
            steps {
                script {
                    // Clone the repository containing the necessary files
                    git branch: 'main', url: 'https://github.com/DanyaHDanny/tafordqe'
                }
            }
        }
        stage('List Host Containers') {
            steps {
                script {
                    // List all active containers on the host machine, jenkins container should be listed
                    sh "curl --unix-socket ${PODMAN_SOCKET} ${PODMAN_API_URL}/containers/json"
                }
            }
        }
        stage('Create PostgreSQL Container') {
            steps {
                script {
                    // Create a new PostgreSQL container, will not cause an error if container name exists
                    sh """
                    curl --unix-socket ${PODMAN_SOCKET} -X POST ${PODMAN_API_URL}/containers/create -H "Content-Type: application/json" -d '{
                        "Image": "postgres:latest",
                        "Name": "postgres_container",
                        "Env": {
                            "POSTGRES_USER": "admin",
                            "POSTGRES_PASSWORD": "admin123",
                            "POSTGRES_DB": "my_database"
                        },
                        "HostConfig": {
                            "PortBindings": {
                                "5432/tcp": [{"HostPort": "5434"}]
                            },
                            "Binds": ["postgres_data:/var/lib/postgresql/data"]
                        }
                    }'
                    """
                }
            }
        }
        stage('Start PostgreSQL Container') {
            steps {
                script {
                    // Extract the container ID and start the PostgreSQL container
                    sh """
                    container_id=\$(curl --unix-socket ${PODMAN_SOCKET} ${PODMAN_API_URL}/containers/json?all=true | jq -r '.[] | select(.Names[0] == "postgres_container") | .Id')
                    if [ -z "\$container_id" ]; then
                        echo "Error: Container ID for 'postgres_container' not found!"
                        exit 1
                    fi
                    curl --unix-socket ${PODMAN_SOCKET} -X POST ${PODMAN_API_URL}/containers/\${container_id}/start
                    """
                }
            }
        }
        stage('Verify PostgreSQL Container') {
            steps {
                script {
                    // Verify that the PostgreSQL container is running
                    sh """
                    container_id=\$(curl --unix-socket ${PODMAN_SOCKET} ${PODMAN_API_URL}/containers/json?all=true | jq -r '.[] | select(.Names[0] == "postgres_container") | .Id')
                    if [ -z "\$container_id" ]; then
                        echo "Error: Container 'postgres_container' does not exist!"
                        exit 1
                    fi
                    echo "Container 'postgres_container' exists with ID: \$container_id"
                    """
                }
            }
        }
    }
}