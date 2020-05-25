import sys
import methods

args = sys.argv[1:] # first arg is filename
if len(args) < 1:
    print("Please provide an accessToken as an.")
    print("Example: python3 clone.py myAccessToken")
    print("\nCreating an access Token")
    print(" > Login to GitHub in your browser")
    print(" > Navigate to this URL https://github.com/settings/tokens")
    print(" > Click Generate New Token")
    print(" > Add a note > select the repo scope > generate token")
    quit()
username = args[0]
accessToken = args[1]
repos = methods.getRepos(accessToken)
for repo in repos:
    methods.cloneRepo(repo)
print("Successfully cloned all of your GitHub repositories")
print("Done.")