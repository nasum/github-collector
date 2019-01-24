import fire

from github import Github

class GithubCollector(object):
  def my_commit(self, start, end):
    print(start)
    
if __name__ == '__main__':
  fire.Fire(GithubCollector)