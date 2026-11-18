import pandas as pd

BAD_DOMAINS = [
    "instagram.com",
    "facebook.com",
    "wa.me",
    "linktr.ee",
    "beacons.ai",
]


def has_real_site(url):

    if pd.isna(url):
        return False

    if not url:
        return False

    url = str(url).lower()

    return not any(
        domain in url
        for domain in BAD_DOMAINS
    )