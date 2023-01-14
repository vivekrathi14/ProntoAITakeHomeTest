# ProntoAITakeHomeTest
Pronto AI's take home test

## Description
This project deals with passing git repository directory path and getting following details
1. Name of active branch of the repository
2. Boolean for local changes made to the files from repository
3. Boolean for whether the latest commit at head is within a week from the date the program
is ran.
4. Boolean for whether the author of the latest commit at head is Rufus.

## Notes
1. In case you added new files to the repo and havent commited the changes, these change is not associated with local changes to existing files and 2. from above doesn't take care
of it.
2. Unit tests have not been written for the tasks in project because it would require some constant repo to check the params. Moreover the GitPython is test proof, where if the git directory path is wrong the program will crash with NoSuchPathError. Any git repo will have atleast one default branch and after cloning it will point to that branch, so we will always have current branch name. Also each git repo will have atleast one commit for the time it was created so the commit object will exist.
3. If you are adding more features to the project with complex functions, it is recommeneded to have unit testing.

## How to use
1. Clone the repo using
`git clone https://github.com/vivekrathi14/ProntoAITakeHomeTest.git`
2. `cd <path to git repo>`
3. Install [miniconda](https://docs.conda.io/en/latest/miniconda.html) if you do not have python
4. Create env using requirements.txt
`conda create --name <env> --file <path to requirements.txt>`
5. cd rufus
6. python rufus.py -p <absolute path to any git repo of interest>

