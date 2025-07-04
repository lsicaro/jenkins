pipeline {
    // Define que nenhum agente principal será usado.
    agent none

    stages {
        stage('1. Checkout do Código') {
            agent any
            steps {
                cleanWs() // A limpeza aqui, no início, é a mais importante.
                git url: 'https://github.com/lsicaro/jenkins.git', branch: 'main'
                echo "Código baixado com sucesso."
            }
        }

        stage('2. Build em Container Docker') {
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo "Iniciando Build em container..."
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
                sh 'python -m unittest discover'
                echo "Testes concluídos."
            }
        }
    }
    
    post {
        // Bloco executado no final do pipeline.
        always {
            // Apenas uma mensagem de finalização.
            echo "Pipeline finalizado."
        }
    }
}