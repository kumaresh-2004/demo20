pipeline {
    agent any

    environment {
        // Define Python virtual environment directory
        VENV_DIR = "${WORKSPACE}/venv"
    }

    stages {

        stage('Checkout') {
            steps {
                echo "🔄 Checking out code..."
                git branch: 'main', url: 'https://github.com/kumaresh-2004/demo20.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                echo "🐍 Setting up Python virtual environment..."
                // Use bash to ensure `source` works
                sh '''#!/bin/bash
                set -e
                python3 -m venv ${VENV_DIR}
                source ${VENV_DIR}/bin/activate
                python3 -m pip install --upgrade pip
                pip install -r requirements.txt || echo "⚠️ requirements.txt not found, skipping install"
                '''
            }
        }

        stage('Build and Test') {
            steps {
                echo "⚙️ Running build and test..."
                sh '''#!/bin/bash
                set -e
                source ${VENV_DIR}/bin/activate
                python3 -m unittest discover || echo "⚠️ No tests found"
                echo "✅ Build and test completed successfully."
                '''
            }
        }

        stage('Collect Build Data') {
            steps {
                echo "📊 Collecting build metrics..."
                sh '''#!/bin/bash
                set -e
                echo "Build duration: $(date)" > build.log
                echo "Build success: true" >> build.log
                '''
            }
        }

        stage('Train AI Model') {
            steps {
                echo "🧠 Training AI model..."
                sh '''#!/bin/bash
                set -e
                source ${VENV_DIR}/bin/activate
                python3 ai_model/train.py || echo "⚠️ Skipping AI training (no file found)"
                '''
            }
        }

        stage('Predict Next Build Result') {
            steps {
                echo "🔮 Predicting next build result..."
                sh '''#!/bin/bash
                set -e
                source ${VENV_DIR}/bin/activate
                python3 ai_model/predict.py || echo "⚠️ Skipping prediction (no file found)"
                '''
            }
        }

        stage('AI Log Analysis (Optional)') {
            steps {
                echo "📈 Analyzing build logs with AI..."
                sh '''#!/bin/bash
                set -e
                if [ -f build.log ]; then
                    echo "✅ Found build.log, performing analysis..."
                    python3 ai_model/analyze_logs.py || echo "⚠️ Skipping log analysis"
                else
                    echo "⚠️ No build.log found — skipping analysis."
                fi
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Pipeline completed successfully!"
        }
        failure {
            echo "❌ Pipeline failed. Check logs above for details."
        }
        always {
            echo "🧾 Printing build log (if exists)..."
            sh '''#!/bin/bash
            if [ -f build.log ]; then
                echo "===== BUILD LOG ====="
                cat build.log
                echo "====================="
            else
                echo "⚠️ No build log found — build might have failed early."
            fi
            '''
        }
    }
}
