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

y = getRepos("f41a94377016c7f40cd5749615d6a8a37f56447a")
for x in y:
    print(x.clone_url)