pipeline {
    agent any

    environment {
        STEAM_USERNAME = credentials('STEAM_USERNAME')
        STEAM_PASSWORD = credentials('STEAM_PASSWORD')
        GIT_CREDENTIAL = '08c5ddf6-53c7-4ef5-b2b7-32f7181f10ad'
    }

    stages {
        stage('Checkout Repository') {
            steps {
                checkout scm
            }
        }

        stage('Clone Repository') {
            steps {
                git credentialsId: "${env.GIT_CREDENTIAL}",
                    url: 'https://github.com/rkorom/hoi4-hun.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    sudo dpkg --add-architecture i386
                    sudo apt-get update
                    sudo apt-get install -y lib32gcc-s1 lib32stdc++6
                '''
            }
        }

        stage('Download and Install SteamCMD') {
            steps {
                sh '''
                    mkdir -p ~/steamcmd
                    cd ~/steamcmd
                    curl -sqL "https://steamcdn-a.akamaihd.net/client/installer/steamcmd_linux.tar.gz" | tar zxvf -
                '''
            }
        }

        stage('Upload to Steam Workshop') {
            steps {
                sh '''
                    if [ ! -f ~/steamcmd/ssfn* ]; then
                        ~/steamcmd/steamcmd.sh +login $STEAM_USERNAME $STEAM_PASSWORD || exit 1
                        # Itt be kell kézzel írni a Steam Guard kódot, ha kéri
                        # A fájlokat későbbi futásokhoz megtartjuk
                    fi

                    ~/steamcmd/steamcmd.sh +login $STEAM_USERNAME $STEAM_PASSWORD +workshop_build_item ${WORKSPACE}/metadata.vdf +quit
                '''
            }
        }

        stage('Logout from Steam') {
            steps {
                sh '''
                    ~/steamcmd/steamcmd.sh +logout
                '''
            }
        }
    }

    post {
        always {
            node {
                cleanWs()
            }
        }
    }
}
