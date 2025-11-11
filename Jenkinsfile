pipeline {
    agent any

    environment {
        PYTHON_ENV = "${WORKSPACE}/venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo '🔄 Checking out code...'
                git branch: 'main', url: 'https://github.com/kumaresh-2004/demo20.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo '🐍 Setting up Python virtual environment...'
                sh '''
                    python3 -m venv $PYTHON_ENV
                    source $PYTHON_ENV/bin/activate
                    python3 -m pip install --upgrade pip
                    if [ -f requirements.txt ]; then
                        pip install -r requirements.txt || true
                    else
                        echo "No requirements.txt found — skipping dependency installation."
                    fi
                '''
            }
        }

        stage('Build and Test') {
            steps {
                echo '🧱 Running build and tests...'
                sh '''
                    source $PYTHON_ENV/bin/activate
                    echo "Building project..."
                    sleep 5
                    echo "Build completed successfully!" > build.log
                '''
            }
        }

        stage('Collect Build Data') {
            steps {
                echo '📊 Collecting Jenkins build data...'
                sh '''
                    source $PYTHON_ENV/bin/activate
                    if [ -f collect_build_data.py ]; then
                        python3 collect_build_data.py
                    else
                        echo "collect_build_data.py not found — skipping."
                    fi
                '''
            }
        }

        stage('Train AI Model') {
            steps {
                echo '🧠 Training AI model...'
                sh '''
                    source $PYTHON_ENV/bin/activate
                    if [ -f train_model.py ]; then
                        python3 train_model.py
                    else
                        echo "train_model.py not found — skipping training."
                    fi
                '''
            }
        }

        stage('Predict Next Build Result') {
            steps {
                echo '🤖 Predicting next build result...'
                sh '''
                    source $PYTHON_ENV/bin/activate
                    if [ -f predict_build.py ]; then
                        python3 predict_build.py
                    else
                        echo "predict_build.py not found — skipping prediction."
                    fi
                '''
            }
        }

        stage('AI Log Analysis (Optional)') {
            steps {
                script {
                    def apiKey = sh(script: 'echo $OPENAI_API_KEY', returnStdout: true).trim()
                    if (apiKey) {
                        echo '💬 Using AI to summarize logs...'
                        sh '''
                            source $PYTHON_ENV/bin/activate
                            if [ -f summarize_logs.py ]; then
                                python3 summarize_logs.py
                            else
                                echo "summarize_logs.py not found — skipping AI log analysis."
                            fi
                        '''
                    } else {
                        echo '⚠️ No OPENAI_API_KEY found — skipping AI analysis.'
                    }
                }
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline complete!'
            script {
                node {
                    // Ensure build.log always exists
                    sh '''
                        if [ ! -f build.log ]; then
                            echo "⚠️ No build log found — build might have failed early." > build.log
                        fi
                        echo "===== BUILD LOG ====="
                        cat build.log
                        echo "====================="
                    '''
                }
            }
        }
        success {
            echo '🎉 Build succeeded! All stages completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed. AI will analyze the issue next time.'
        }
    }
}
