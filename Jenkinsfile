// Declarative Jenkins pipeline — mirrors the GitHub Actions workflow.
// Demonstrates the same CI/CD stages in a self-hosted CI server.
//
// Required Jenkins credentials (Manage Jenkins → Credentials):
//   - dockerhub-creds   : Username/Password credential for Docker Hub
//   - render-deploy-hook : Secret text — your Render deploy hook URL
//   - slack-webhook      : Secret text — (optional) Slack incoming webhook

pipeline {
  agent any

  environment {
    IMAGE_NAME = 'cicd-demo'
    // Jenkins exposes the build number as BUILD_NUMBER automatically.
  }

  options {
    timestamps()
    disableConcurrentBuilds()
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    // ---------- STAGE 1: Quality gate (lint + test) ----------
    stage('Lint & Test') {
      steps {
        sh 'npx --yes htmlhint "site/**/*.html"'
        sh 'node tests/smoke.test.js'
      }
    }

    // ---------- STAGE 2: Build & push Docker image ----------
    stage('Build & Push Image') {
      when { branch 'main' }
      steps {
        // Inject build metadata into the page.
        sh '''
          sed -i "s/__BUILD_NUMBER__/${BUILD_NUMBER}/" site/app.js
          sed -i "s/__COMMIT_SHA__/$(git rev-parse HEAD)/" site/app.js
        '''
        withCredentials([usernamePassword(
          credentialsId: 'dockerhub-creds',
          usernameVariable: 'DOCKERHUB_USERNAME',
          passwordVariable: 'DOCKERHUB_TOKEN'
        )]) {
          sh '''
            echo "$DOCKERHUB_TOKEN" | docker login -u "$DOCKERHUB_USERNAME" --password-stdin
            docker build -t "$DOCKERHUB_USERNAME/$IMAGE_NAME:latest" \
                         -t "$DOCKERHUB_USERNAME/$IMAGE_NAME:${BUILD_NUMBER}" .
            docker push "$DOCKERHUB_USERNAME/$IMAGE_NAME:latest"
            docker push "$DOCKERHUB_USERNAME/$IMAGE_NAME:${BUILD_NUMBER}"
          '''
        }
      }
    }

    // ---------- STAGE 3: Deploy to Render ----------
    stage('Deploy to Render') {
      when { branch 'main' }
      steps {
        withCredentials([string(
          credentialsId: 'render-deploy-hook',
          variable: 'RENDER_DEPLOY_HOOK'
        )]) {
          sh 'curl -fsSL -X POST "$RENDER_DEPLOY_HOOK"'
          echo 'Deploy triggered on Render.'
        }
      }
    }
  }

  // ---------- STAGE 4: Notify ----------
  post {
    success {
      echo 'Pipeline succeeded ✅'
      notifySlack('✅ Success')
    }
    failure {
      echo 'Pipeline failed ❌'
      notifySlack('❌ Failed')
    }
  }
}

// Helper: posts to Slack only if the webhook credential exists.
def notifySlack(String status) {
  try {
    withCredentials([string(credentialsId: 'slack-webhook', variable: 'SLACK_WEBHOOK')]) {
      sh """
        curl -fsSL -X POST -H 'Content-type: application/json' \
          --data '{"text":"CI/CD Pipeline (Jenkins): ${status} — build #${BUILD_NUMBER}"}' \
          "\$SLACK_WEBHOOK"
      """
    }
  } catch (err) {
    echo "Slack notification skipped (no webhook configured)."
  }
}
