'''
This one is to note the basic commands of git and github

Configuring git - 

git config --global user.name "My Name"
git config --global usee.email "email_address"
git config --lis

Cloning a new repo in the local repository -
    git clone <https_link>

    git status

[Git statuses - 
    untracked [new files that git doesn't yet track] 
    modified [changes]
    staged [file ready to be commited]
    unmodified [unchanged]]

git add <file_name>
git commit -m "change message"
git oush origin <branch_name>


Init command - [used to creat a new git reopo]
    git init
    git remote add origin <link> [remote ist he repository staroed remotely, like on github]
    git remote -v [to verify remote]
    
    git branch [to check branch]
    git branch -M main [to rename branch]
    git push origin main 

    
Branch commands -
    git branch [to check branch]
    git branch -M main [to rename branch name]
    git checkout <branch_name> [to navigate]
    git checkout -b <new branch name> [to create new branch]
    git branch -f <branch name> [to delete branch]
    
'''
