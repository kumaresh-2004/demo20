pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/kumaresh-2004/demo20.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Build and Test') {
            steps {
                echo '🧱 Running build and tests...'
                // simulate build
                sh 'sleep 5 && echo "Build completed!" > build.log'
            }
        }

        stage('Collect Build Data') {
            steps {
                echo '📊 Collecting Jenkins build history...'
                sh 'python3 collect_build_data.py'
            }
        }

        stage('Train AI Model') {
            steps {
                echo '🧠 Training AI model...'
                sh 'python3 train_model.py'
            }
        }

        stage('Predict Next Build Result') {
            steps {
                echo '🤖 Predicting next build result...'
                sh 'python3 predict_build.py'
            }
        }

        stage('AI Log Analysis (Optional)') {
            steps {
                script {
                    def hasKey = sh(script: 'echo $OPENAI_API_KEY', returnStdout: true).trim()
                    if (hasKey) {
                        echo '💬 Summarizing logs using GPT...'
                        sh 'python3 summarize_logs.py'
                    } else {
                        echo '⚠️ Skipping AI summarization (no API key found).'
                    }
                }
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline complete!'
        }
    }
}
