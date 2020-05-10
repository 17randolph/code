#!python3

""" This script uploads important dotfiles located at /home/$USER/* to github.
 It is designed specifically for linux systems. Adding file names to the list
 'dotfilesToBackup' will add the dotfiles to a github repository named '/dotfiles' """

import os
import getpass
from github import Github
from github import GithubException

# get current user's directory
user = getpass.getuser()
directory = ("/home/" + user + "/")
files = os.listdir(directory)

# list of important dotfiles to upload to github
dotfilesToBackup = ['.bashrc', '.profile']

# github access token
g = Github("token")
gitUser = g.get_user()

# check to see if '/dotfiles' is already a repository, create it if not
repoList = []
for repo in gitUser.get_repos():
    repoList.append(repo.name)

if "dotfiles" not in repoList:
    print("'/dotfiles' does not exist, creating /dotfiles")
    repo = gitUser.create_repo("dotfiles", description = "dotfile backups from linux distro")

# add or update files into repository
repo = g.get_repo(gitUser.login+"/dotfiles")

try:
    contents = repo.get_contents("")
except GithubException as e:
    print(e.args[1]['message'])  # output: this repository is empty
    contents = []

repoContents = []
for content in contents:
    repoContents.append(content.name)

for file in files:
    if file in dotfilesToBackup and not repoContents:
        with open(directory + file) as input_file:
            data = input_file.read()
            print("Adding", file, "to", "/dotfiles")
            repo.create_file(file, 'dotfile', data)
    elif file in dotfilesToBackup and repoContents:
        with open(directory + file) as input_file:
            data = input_file.read()
            ghfile = repo.get_file_contents(file)
            print("Updaing", file, "in", "/dotfiles")
            repo.update_file(file, 'dotfile', data, ghfile.sha)
