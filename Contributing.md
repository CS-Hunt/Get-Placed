#
<div align="center">
<img src=".app/static/images/logo.jpeg" width="20%">
<b>
</b>
<h1>Welcome to the Get Placed Repository</h1>

<a href="https://t.me/joinchat/YKR5_lOCNppiZjNl">![Telegram Community](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)</a>
<a href="mailto:info.cshunt@gmail.com">![Gmail](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)</a>
<a href="https://open.vscode.dev/CS-Hunt/Get-Placed.git"><img src="https://open.vscode.dev/badges/open-in-vscode.svg" height="25px"></a>

</div>

<br/>

A big welcome to Get Placed ! 
<br />
Thank you for considering contributing to Get Placed !
<br />
It’s because of people like you that open source projects emerge ! 

#

### Table of contents

- Contributing to Get Placed

      - Getting Started
      - Issues
      - Pull Requests
      - Merging Pull Requests

- NB  

      - Fork-and-Pull
      - Getting Help

#

### Getting Started

Contributions are made to this repo via Issues and Pull Requests (PRs).
<br />
<br/>
To contribute :

- Search for **existing Issues and PRs before creating your own**.
- Describe your changes & issues very well by **following our PR & issues templates !**

#

### Issues

Issues are used to report problems with the library, request a new feature, or to discuss potential changes before a PR is created.

If you find an issue that addresses the problem you're having, please complete this issue with comments.
<br />
You can send screenshots to further explain the bug you are encountering. 

Before you make your changes, please open an issue. We'll use the issue to have a conversation about the feature or problem and how you want to go about it. 

**Please don't work on said issue until you have been assigned to it.**

#

### Pull Requests

PRs are always welcome !
<br />
<br />
In general, PRs should:

- Only fix/add the functionality in question **OR** address wide-spread whitespace/style issues, not both.
- **Add unit or integration tests for fixed or changed functionality** (if a test suite already exists).
- Address a single concern in the least number of **changed lines as possible**.
- **Be accompanied by a complete Pull Request template (loaded automatically when a PR is created)**.
#

### Merging Pull Requests


1. It's mandatory that the PR author adds reviewers prior to submitting the PR. Tag reviewers in the message. A collaborator of the repo will officially add them in PR as reviewer(s). 
2. All PRs will require the approval of both reviewers prior to the branch merge. Once the last reviewer approves the changes, they can merge the branch.
3. The PR author should **add two reviewers; unless the change is so minor (think documentation, code formatting)**. A collaborator will choose a label "Review: Needs 1" **OR** "Review: Needs 2" to further organize the repo and review system.

#

### NB

In general, we follow the **fork-and-pull**


#### Steps :

**1. Fork the repository to your own Github account**

**2. Clone the forked project to your machine**

   ```bash
    git clone https://github.com/<your-github-username>/Get-Placed.git
   ```

**3.Add Upstream or the remote of the original project to your local repository**

   ```bash
   # check remotes
   git remote -v
   git remote add upstream https://github.com/CS-Hunt/Get-Placed.git
   ```

**4. Make sure you update the local repository**

   ```bash
   # Get updates
   git fetch upstream
   # switch to master branch
   git checkout master
   # Merge updates to local repository
   git merge upstream/master
   # Push to github repository
   git push origin master
   ```

**5. Create a branch locally with a succinct but descriptive name**

   ```bash
   git checkout -b branch-name
   ```

**6. Commit changes to the branch**

   ```bash
   # Stage changes for commit i.e add all modified files to commit
   git add .
   # You can also add specific files using
   # git add <filename1> <filename2>
   git commit -m "your commit message goes here"
   # check status
   git status
   ```

**7.Following any formatting and testing guidelines specific to this repository**

**8. Push changes to your fork**

   ```bash
   git push origin branch-name
   ```

**9.Open a PR in our repository and follow the PR template so that we can efficiently review the changes.**

**10. After the pull request was merged, fetch the upstream and update the default branch of your fork**

#

### Getting Help

Join us in **[the Telegram Server](https://t.me/joinchat/YKR5_lOCNppiZjNl)** and post your question there in the correct category with a descriptive tag.

#
