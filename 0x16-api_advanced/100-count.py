import requests

def count_words(subreddit, word_list, after=None, counts={}):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Custom-User-Agent"}
    params = {"after": after} if after else {}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        
        for post in posts:
            title = post['data']['title'].lower()
            for word in word_list:
                if word.lower() in title:
                    counts[word.lower()] = counts.get(word.lower(), 0) + 1
        
        after = data['data']['after']
        
        if after:
            return count_words(subreddit, word_list, after, counts)
        else:
            sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                print(f"{word}: {count}")
    else:
        raise Exception(f"Error accessing subreddit. Status code: {response.status_code}")

# Example usage
subreddit_name = "python"
keyword_list = ["python", "java", "javascript"]

count_words(subreddit_name, keyword_list)
