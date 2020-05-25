import os
from github import Github
from getpass import getpass



def getRepos(accessToken):
    print("Retrieving your GitHub repositories")
    gh = Github(accessToken)
    return gh.get_user().get_repos()

def cloneRepo(repo):
    print("Cloning {}".format(repo.name))
    giturl = repo.clone_url
    stream = os.popen('git clone {}'.format(giturl))
    output = stream.read()
    print("Cloned {}".format(repo.name))
