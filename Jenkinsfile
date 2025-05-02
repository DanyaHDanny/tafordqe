pipeline {
    agent any
    stages {
        stage('Update Packages') {
            steps {
                script {
                    // Update the package list
                    sh 'apt-get update'
                }
            }
        }
        stage('Install Python') {
            steps {
                // Install Python and pip
                sh 'apt-get install -y python3 python3-pip'
                sh 'apt-get install -y python3.11-venv'
                //sh 'ln -s /usr/bin/python3 /usr/bin/python'
            }
        }
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository
                git branch: 'main', url: 'https://github.com/DanyaHDanny/tafordqe'
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                    // Create a virtual environment
                    sh 'apt-get install -y libpq-dev'
                    sh '''
                        python3 -m venv venv
                        source venv/bin/activate
                        pip install -r tafordqe/data_dev/requirements.txt
                    '''
                }
            }
        }
        stage('Run main') {
            steps {
                script {
                    // Activate the virtual environment and run the Python script
                    sh '''
                        source venv/bin/activate
                        python tafordqe/data_dev/main.py
                    '''
                }
            }
        }
    }
    post {
        always {
            echo 'Pipeline execution completed.'
        }
        success {
            echo 'Pipeline executed successfully!'
        }
        failure {
            echo 'Pipeline failed. Please check the logs for details.'
        }
    }
}


