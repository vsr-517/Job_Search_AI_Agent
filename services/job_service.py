import requests

from config import ADZUNA_APP_ID, ADZUNA_APP_KEY


class JobAPIError(Exception):
    """Raised when the Adzuna API request fails."""


def search_jobs(
    query: str = "python developer",
    location: str = "India",
    results_count: int = 5,
) -> list[dict]:
    query = query.strip()
    location = location.strip()

    if not query:
        raise ValueError("Job role cannot be empty.")

    if not location:
        raise ValueError("Location cannot be empty.")

    if not ADZUNA_APP_ID or not ADZUNA_APP_KEY:
        raise JobAPIError("Adzuna API credentials are missing.")

    try:
        results_count = int(results_count)
    except (TypeError, ValueError) as error:
        raise ValueError("Results count must be a number.") from error

    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "results_per_page": results_count,
        "what": query,
        "where": location,
        "content-type": "application/json",
    }

    try:
        response = requests.get(url, params=params, timeout=20)
        response.raise_for_status()
    except requests.exceptions.Timeout as error:
        raise JobAPIError("Job search timed out. Please try again.") from error
    except requests.exceptions.RequestException as error:
        raise JobAPIError(f"Job search failed: {error}") from error

    data = response.json()
    return data.get("results", [])