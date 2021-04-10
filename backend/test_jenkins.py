from jenkinsapi.jenkins import Jenkins
def test_jenkins():
    jenkins = Jenkins(
        'http://localhost:8080/jenkins/',
        username = "ygl",
        password = ""
    )
    print(jenkins.keys())