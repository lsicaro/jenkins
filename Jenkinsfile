pipeline {
    agent any

    stages {
        stage('1. Checkout do Código') {
            steps {
                // Limpa o workspace antes de baixar o código
                cleanWs()
                // Clona o repositório do GitHub
                git credentialsId: 'github-credentials', url: 'https://github.com/lsicaro/jenkins', branch: 'main'
                echo "Código baixado com sucesso."
            }
        }

        stage('2. Build em Container Docker') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo "Iniciando Build em container..."
                echo "ID do Container: ${env.DOCKER_CONTAINER_ID.take(12)}"
                sh 'python -m py_compile *.py'
                
                echo "Build (verificação de sintaxe) concluído com sucesso."
            }
        }

        stage('3. Testes em Container Docker') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo "Iniciando Testes em um container isolado..."
                echo "ID do Container: ${env.DOCKER_CONTAINER_ID.take(12)}"
                sh 'python -m unittest discover'
                
                echo "Testes concluídos."
            }
        }
    }
    
    post {
        // Bloco executado no final do pipeline, independentemente do resultado
        always {
            echo "Pipeline finalizado."
            // Limpa o workspace para a próxima execução
            cleanWs()
        }
    }
}