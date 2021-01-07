import os

## Number of days you want to make commits
for i in range(28*2 + 10,58*2 + 1):
    d = str(i) + ' day ago'
    ## Open a text file and modify it
    with open('getdata.php', 'a') as file:
        file.write(d)
    ## Add bot.txt to staging area
    os.system('git add getdata.php')
    ## Commit it
    os.system('git commit --date="' + d + '" -m "#commit"')

## push the commit to github
os.system('git push origin HEAD:A')
