pipeline {
    agent any
    environment {
        TARGET_NAME = "gaore_developer_doc.tar.gz"
    }

    stages {
        stage("install_plugin") {
            steps {
                echo "start to install plugin"
                sh "gitbook install"
                echo "install plugin success"
            }
        }
     
        stage("build_book") {
            steps {
                echo "start to build book"
                sh "gitbook build ."
                echo "build gitbook success"
            }
        }

        stage("remove_useless_file") {
            steps {
                sh "rm -f ./_book/Jenkinsfile"
                sh "rm -f ./_book/requirements.txt"
                sh "rm -f ./_book/upload_sdk_resource.py"
                sh "rm -f ./_book/.gitignore"
                sh "rm -f ${TARGET_NAME}"
            }
        }

        stage("artifacts") {
            steps {
                echo "artifacts book"
                sh "tar zcvf ${TARGET_NAME} ./_book"
                archiveArtifacts artifacts: "${TARGET_NAME}", fingerprint: true, onlyIfSuccessful: true
                sh "rm ${TARGET_NAME}"
            }
        }

        stage("deploy_book") {
            steps {
                script {
                    if (branch_name == "master") {
                        echo "delete server old book and scp new book to server"
                        sh "ssh work@111.230.14.30 rm -rf /work/gaore_dev_doc && \
                            scp -r ./_book work@111.230.14.30:/work/gaore_dev_doc && \
                            ssh work@111.230.14.30 /work/shell/restart_doc_server.sh"
                    }
                }
            }            
        }
    }
}

