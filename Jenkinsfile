pipeline{

    agent any

	environment {
		//DB_FILES_HOME = "/home/pi/Development/segura/database/"
		//DB_FILES_MYSQL = "DB_FILES_HOME/provision_myql/"
		//HELLO_WORLD = "C:\\Users\\Erik\\PycharmProjects\\segura\\helloWorld.py"
	}

    stages{
        stage('Checkout'){
            steps{
                checkout(
                    [
                        $class: 'GitSCM',
                        branches: [[name: '*/dev']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        submoduleCfg: [],
                        userRemoteConfigs: [[credentialsId: 'GitHub', url: 'https://github.com/vanroon/segura.git']]
                    ]
                )
            }
        }
        stage('Say "hello world"'){
            steps{
                powershell './hw_powershell.ps1'
                powershell './helloWorld.ps1'
            }
        }
        stage('Process source files'){
            steps{
                echo "1. execute python script. Input: all source csv's. Output one noDupMasterCsvFile"
            }
        }
	    stage('Build database') {
	        steps{
	            echo 'Building...'
	            echo "This are the database files: \n $DB_FILES_HOME"
	            echo "build tables"
	            echo "build views and others"
	        }
	    }
	    stage('Provision database'){
	        steps{
	            echo 'Provisioning...'
	            echo "Input is noDupMasterCsvFile"
	        }
	    }
	}
}
