pipeline 
{
    agent 
    {
        docker { image 'python:3.6.10' } 
    }
    stages 
    {
        stage('build_project') 
        {
            steps 
            {
                sh 'python3 -m pip install robotframework'
                sh 'pip install docutils'
                sh 'robot pipline/my.rst' 
            }
        }
    }
}
