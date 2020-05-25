import os
from getpass import getpass
    

def cloneRepo(repo):
    print("Cloning {}".format(repo.name))
    giturl = repo.clone_url
    stream = os.popen('git clone {}'.format(giturl))
    output = stream.read()
    print("Cloned {}".format(repo.name))
