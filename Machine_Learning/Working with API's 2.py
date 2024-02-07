import requests
import pandas as pd

# JSON ----> JavaScript Object Notation ({})
url = "https://api.github.com/users/LeonardLeo"
url1 = "https://api.github.com/users/LeonardLeo/repos"

# Get Leo's data
scraper = requests.get(url)
response = scraper.json()

# Get info on all Leo's Repos
scraper1 = requests.get(url1)
response1 = scraper1.json()

# dataset_repos = pd.DataFrame(response1)

# # Creating a dataset that shed's light on LEO and his repo
# owner_leo = pd.Series([data for data in dataset_repos.loc[:, "owner"]][0])
# dataset_repos = dataset_repos.drop("owner", axis = 1)




# CREATING A LOOP THAT GETS DATA ON EVERYONE
github_dataset = pd.DataFrame(columns = [key for key in response.keys()])
GithubUsers = ["hnry-dngr", "orbituser", "Busola8", "Zanniey"]
for user in GithubUsers:
    user_url = f"https://api.github.com/users/{user}"
    github_scraper = requests.get(user_url)
    github_response = github_scraper.json()
    github_response_values = pd.DataFrame(github_response)
    pd.concat([github_dataset, github_response_values])
