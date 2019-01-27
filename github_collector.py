import os
import fire

from github import Github


class GithubCollector(object):

    def my_commit(self, start=None, end=None):
        g = Github(os.environ['GITHUB_ACCESS_TOKEN'])
        user = g.get_user()
        for repo in user.get_repos(sort='pushed'):
            for commit in repo.get_commits(author=user):
                print(commit.html_url)


if __name__ == '__main__':
    fire.Fire(GithubCollector)
