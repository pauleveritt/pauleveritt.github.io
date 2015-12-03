import requests
from typing import List


class GitHubEvent:
    def __init__(self, feed_id: int, author: str):
        self.feed_id = feed_id
        self.author = author

    def __str__(self):
        return 'Feed Item {id} by {author}'.format(id=self.feed_id,
                                                   author=self.author)


class GitHubEvents:
    def __init__(self, url: str):
        self.url = url

    def list(self) -> List[GitHubEvent]:
        r = requests.get(self.url)
        items = r.json()
        return [
            GitHubEvent(int(i['id']), i['actor']['login']) for i in
            items]


# As the consumer of the above "library" would see it
def main():
    url = 'https://api.github.com/events'
    f = GitHubEvents(url)
    feed_items = f.list()
    print(feed_items[0])


if __name__ == '__main__':
    main()
