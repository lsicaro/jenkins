pipeline {
    // Define que nenhum agente principal será usado, evitando o checkout duplo.
    agent none

    stages {
        stage('1. Checkout do Código') {
            // Um agente simples apenas para baixar o código.
            agent any
            steps {
                cleanWs()
                git url: 'https://github.com/lsicaro/jenkins.git', branch: 'main'
                echo "Código baixado com sucesso."
            }
        }

        stage('2. Build em Container Docker') {
            // Define que este estágio rodará dentro de um container Docker.
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo "Iniciando Build em container..."
                // Nosso "build" para Python será verificar a sintaxe dos arquivos.
                sh 'python -m py_compile *.py'
                echo "Build (verificação de sintaxe) concluído com sucesso."
            }
        }

        stage('3. Testes em Container Docker') {
            // Um NOVO container será iniciado para este estágio.
            agent {
                docker { image 'python:3.9-slim' }
            }
            steps {
                echo "Iniciando Testes em um container isolado..."
                // Executa os testes unitários.
                sh 'python -m unittest discover'
                echo "Testes concluídos."
            }
        }
    }
    
    post {
        // Bloco executado no final do pipeline.
        always {
            echo "Pipeline finalizado."
            cleanWs()
        }
    }
}