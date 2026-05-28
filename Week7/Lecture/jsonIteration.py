import requests

results = requests.get(
    "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow&pagesize=10&page=1"
)
# print(type(results))
# print(dir(results))

results = results.json()
print(type(results))

if "items" in results:
    for question in results["items"]:
        if "user_id" in question["owner"] and "reputation" in question["owner"]:
            print(f'user id is {question["owner"]["user_id"]}')
            print(f'reputation is {question["owner"]["reputation"]}')
