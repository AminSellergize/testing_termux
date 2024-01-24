import subprocess

def fetch_dom(url):
    try:
        # Use subprocess to run the curl command and capture the output
        result = subprocess.run(['curl', url], capture_output=True, text=True)

        # Check for errors in the result
        if result.returncode == 0:
            # Print the HTML content
            print(result.stdout)
        else:
            print(f"Error: {result.stderr}")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace 'https://example.com' with the URL of the website you want to fetch
    website_url = 'https://example.com'
    fetch_dom(website_url)
