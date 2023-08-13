import os
from serpapi import GoogleSearch
import key

key.setenv()

params = {
  "engine": "google",
  "q": "2023年4月現在の首相の名前について",
  "location": "Tokyo",
  "hl": "ja",
  "gl": "jp",
  "google_domain": "google.co.jp",
  "num": "3",
  "start": "10",
  "safe": "active",
  "api_key": "{}".format(os.getenv("SERPAPI_KEY"))
}

search = GoogleSearch(params)
results = search.get_dict()
organic_results = results["organic_results"]
print(organic_results)