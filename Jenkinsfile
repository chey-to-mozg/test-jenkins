pipeline 
{
    agent 
    {
        docker { image 'python:3.6.10' } 
    }
    stages 
    {
        stage('build_test') 
        {
            steps 
            {
                sh 'python3 -m pip install robotframework'
            }
        }
    }
}
