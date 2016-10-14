def registryTag = 'trex-demo-stage/service-a:latest'
def dockerServer = 'tcp://192.168.100.160:2375'
node {
	stage('Checkout') {
		checkout scm
		sh 'ls -la'
		sh "echo \"VERSION = ${env.BUILD_NUMBER}\" > version.py"
	}
	
	def app = null
	docker.withServer(dockerServer) {
		
		stage('Build Docker') {
			app = docker.build "192.168.100.160:5000/${registryTag}"
		}
		stage('Unit Test') {
			
			sshagent(['ssh-cred-1']) {
				def testResult = sh(script: "ssh -o StrictHostKeyChecking=no -l englishja 192.168.100.160 docker run 192.168.100.160:5000/${registryTag} ./test.sh", returnStdout: true).trim()
			
				echo testResult
			}
			
			//app.withRun('-p 9393:8080 -e IS_TESTING=True','./test.sh') { c ->
			//	sleep 60
			//	sh "wget 192.168.100.160:9393/test"
			//}
			
			//def testResult = sh(script: "sudo docker -H ${dockerServer} run 192.168.100.160:5000/${registryTag} ./test.sh", returnStdout: true).trim()
			
			//echo testResult
			sh 'ls -la'
			//junit 'nose2-junit.xml'
		}

		stage('Staging Environment') {
			app.push()
			sshagent(['ssh-creds']) {
				sh "ssh -o StrictHostKeyChecking=no -l saicadm 192.168.100.80 sudo docker pull 192.168.100.160:5000/${registryTag}"
				sh "ssh -o StrictHostKeyChecking=no -l saicadm 192.168.100.80 sudo docker tag -f 192.168.100.160:5000/${registryTag} 172.30.122.20:5000/${registryTag}"
				def token = sh(script: 'ssh -o StrictHostKeyChecking=no -l saicadm 192.168.100.80 oc whoami -t', returnStdout: true).trim()
				echo token
				sh "ssh -o StrictHostKeyChecking=no -l saicadm 192.168.100.80 \"sudo docker login -u test -e test@test.com -p ${token} 172.30.122.20:5000 && sudo docker push 172.30.122.20:5000/${registryTag}\""
			}
		}


	}
}
	
