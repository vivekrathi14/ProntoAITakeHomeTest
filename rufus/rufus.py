#!/usr/bin/env python 

import argparse
from git import Repo
from datetime import datetime

class GitRepository:
    '''
    Defines class GitRepository
    @param repo_path - absolute path to git repository
    '''
    def __init__(self,repo_path):
        self.repo = Repo(repo_path)
        self.head_commit = self.repo.head.commit
        self.week_days = 7
        self.rufus_name = "rufus"
    
    # Returns the active branch of the repository.
    def get_active_branch(self):
        return self.repo.active_branch
    
    # Returns True if there are any local changes to repository else False
    def get_local_changes(self):
        return True if self.head_commit.diff(None) else False
    
    # Returns True if the head commit was authored within the last 7 days else False
    def is_head_updated_in_week(self):
        now = datetime.utcnow()
        diff = now - self.head_commit.authored_datetime.replace(tzinfo=None)
        return diff.days < self.week_days
    
    # Returns True if the author of the head commit contains "rufus" in their name else False
    def is_author_rufus(self):
        return self.rufus_name in str(self.head_commit.author).lower().split(" ")


if __name__ == "__main__":
    # parses an argument for a path to a git repository
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--path",required=True, help = "Absolute path to the git rep")
    args = parser.parse_args()
    if args.path:
        print("git directory path: {}".format(args.path))
        git_repo = GitRepository(args.path)
        print("active branch: {}".format(git_repo.get_active_branch()))
        print("local changes: {}".format(git_repo.get_local_changes()))
        print("recent commit: {}".format(git_repo.is_head_updated_in_week()))
        print("blame Rufus: {}".format(git_repo.is_author_rufus()))
    else:
        print("Please pass absolute git repo path using -p flag. Thanks!")

        


