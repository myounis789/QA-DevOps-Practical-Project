pipeline {
    agent any
    stages{
        // stage('Run service tests') {
        //     steps{
        //         sh "bash test.sh"
        //     }
        // } 
        stage ('Build and push images to docker') {
            environment {
                DOCKER_UNAME = credentials('docker_uname')
                DOCKER_PWORD = credentials('docker_pword')
            }
            steps {
                sh "docker-compose build --parallel"
                sh "docker login -u $DOCKER_UNAME -p $DOCKER_PWORD"
                sh "docker-compose push"          
            }
        }
        stage ("Run ansible and deploy") {
            steps{
                sh "scp -o StrictHostKeyChecking=no docker-compose.yaml ansible-jenkins:/home/jenkins/docker-compose.yaml"
                sh "ansible-playbook -v -i Ansible/inventory.yaml Ansible/playbook.yaml"
            }
        }
    }
}