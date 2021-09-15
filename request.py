import requests

request_repos = requests.get("https://api.github.com/users/williamchenghu/repos")
repositories = request_repos.json()

for repo in repositories:
    print(f"Repo Name: {repo['name']}\nRepo URL: {repo['html_url']}\n")
