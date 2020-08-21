git branch | grep -v "master" | xargs git branch -D
git remote prune origin