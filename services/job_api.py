import requests
from config import ADZUNA_APP_ID, ADZUNA_APP_KEY

def search_jobs(query="python developer", location="India"):
    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": 5,
        "what": query,
        "where": location,
        "content-type": "application/json"
    }

    try:
        response = requests.get(url, params=params, timeout=15)

        print("Status Code:", response.status_code)

        if response.status_code == 200:
            data = response.json()
            return data.get("results", [])

        elif response.status_code == 503:
            print("Adzuna server is temporarily unavailable. Try again after few minutes.")
            return []

        else:
            print("Error:", response.text[:300])
            return []

    except requests.exceptions.RequestException as e:
        print("Network/API error:", e)
        return []


if __name__ == "__main__":
    jobs = search_jobs("data analyst", "India")

    print("Jobs Found:", len(jobs))

    for job in jobs:
        print("--------------------")
        print("Title:", job.get("title"))
        print("Company:", job.get("company", {}).get("display_name"))
        print("Location:", job.get("location", {}).get("display_name"))
        print("URL:", job.get("redirect_url"))