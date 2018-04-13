### Forking the Project

#### Setting Up Your System

1. Install [Git](https://git-scm.com/) or your favorite Git client.
2. (Optional) [Setup an SSH Key](https://help.github.com/articles/generating-an-ssh-key/) for GitHub.

#### Forking project

1. Go to the top level repository: <git@github.com:nmttoan/python.git>
2. Click the "Fork" Button in the upper right hand corner of the interface ([More Details Here](https://help.github.com/articles/fork-a-repo/))
3. After the repository (repo) has been forked, you will be taken to your copy of the project repo at <https://github.com/yourUsername/python>

#### Cloning Your Fork

1. Open a Terminal / Command Line / Bash Shell in your projects directory (_i.e.: `/yourprojectdirectory/`_)
2. Clone your fork of project

```shell
$ git clone https://github.com/yourUsername/python.git
```

**(make sure to replace `yourUsername` with your GitHub username)**

This will download the entire project repo to your projects directory.

#### Setup Your Upstream

1. Change directory to the new project directory (`cd project`)
2. Add a remote to the official project repo:

```shell
$ git remote add upstream https://github.com/nmttoan/python.git
```

Congratulations, you now have a local copy of the project repo!

#### Maintaining Your Fork

Now that you have a copy of your fork, there is work you will need to do to keep it current.

##### Rebasing from Upstream

Do this prior to every time you create a branch for a PR:

1. Make sure you are on the `staging` branch

```shell
$ git status
On branch staging
Your branch is up-to-date with 'origin/staging'.
```
If your aren't on `staging`, resolve outstanding files / commits and checkout the `staging` branch

```shell
$ git checkout staging
```

2. Do a pull with rebase against `upstream`

```shell
$ git pull --rebase upstream staging
```

This will pull down all of the changes to the official staging branch, without making an additional commit in your local repo.

3. (_Optional_) Force push your updated staging branch to your GitHub fork

```shell
$ git push origin staging --force
```

This will overwrite the staging branch of your fork.

### Create a Branch

Before you start working, you will need to create a separate branch specific to the issue / feature you're working on. You will push your work to this branch.

#### Naming Your Branch

Name the branch something like `fix/xxx` or `feature/xxx` where `xxx` is a short description of the changes or feature you are attempting to add. For example `fix/email-login` would be a branch where you fix something specific to email login.

#### Adding Your Branch

To create a branch on your local machine (and switch to this branch):

```shell
$ git checkout -b [name_of_your_new_branch]
```

and to push to GitHub:

```shell
$ git push origin [name_of_your_new_branch]
```

**If you need more help with branching, take a look at [this](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches).**

### Set Up Linting

We prefered Visual Studio Code to maintain the project.
You should have [Flake8 linting running in your editor](https://code.visualstudio.com/docs/python/linting), and it will highlight anything doesn't conform to project's Python Style Guide.


> Please do not ignore any linting errors, as they are meant to **help** you and to ensure a clean and simple code base.
