import sys
import methods
from github import Github


args = sys.argv[1:] # first arg is filename
if len(args) < 1:
    print("Please provide an accessToken as an argument.")
    print("Example: python3 clone.py myAccessToken")
    print("\nCreating an access Token")
    print(" > Login to GitHub in your browser")
    print(" > Navigate to this URL https://github.com/settings/tokens")
    print(" > Click Generate New Token")
    print(" > Add a note > select the repo scope > generate token")
    quit()
accessToken = args[0]

print("Retrieving your GitHub repositories")
gh = Github(accessToken)
repos = gh.get_user().get_repos()
for repo in repos:
    methods.cloneRepo(repo)
print("Successfully cloned all of your GitHub repositories")
print("Done.")