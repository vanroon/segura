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
                        branches: [[name: '*/master']],
                        doGenerateSubmoduleConfigurations: false,
                        extensions: [],
                        submoduleCfg: [],
                        userRemoteConfigs: [[credentialsId: 'GitHub', url: 'https://github.com/vanroon/segura.git']]
                    ]
                )
            }
        }
        stage('prepare noDup master csv'){
            steps{
              // 1. execute python script to create master csv file and remove duplicates
              // 2. execute shell script to remove quotes around money field
            }
        }
        stage('Build container'){
            steps{
              // 3. move nodup master to docker psql data dir to include it the build.
              // 4. build container
            }
        }
	    stage('Build database') {
	        steps{
	            // echo 'Building...'
	            // echo "This are the database files: \n $DB_FILES_HOME"
	            // echo "build tables"
	            // echo "build views and others"
	        }
	    }
	    stage('Provision database'){
	        steps{
	            // echo 'Provisioning...'
	            // echo "Input is noDupMasterCsvFile"
	        }
	    }
	}
}
