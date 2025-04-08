import http.client
import json

def fetch_metadata(path=""):
    conn = http.client.HTTPConnection("169.254.169.254", timeout=2)
    conn.request("GET", f"/latest/meta-data/{path}")
    res = conn.getresponse()

    if res.status != 200:
        raise Exception(f"Failed to get metadata: {res.status} {res.reason}")

    data = res.read().decode()
    return data

def fetch_all_metadata():
    try:
        metadata_keys = fetch_metadata().splitlines()
        metadata = {key: fetch_metadata(key) for key in metadata_keys}
        print(json.dumps(metadata, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    fetch_all_metadata()
