import os
import fire

from github import Github
from github.Repository import Repository


class GithubCollector(object):

    def my_commit(self, start=None, end=None):
        g = Github(os.environ['GITHUB_ACCESS_TOKEN'])
        for repo in g.get_user().get_repos(sort='pushed'):
            print(repo.name)


if __name__ == '__main__':
    fire.Fire(GithubCollector)