import os
from random import randint
for i in range(1,465):
    for j in range(0,randint(1,10)):
        d = str(i)+'days ago'
        with open('file.txt','a') as file:
            file.write(d)
        os.system('git add .')
        os.system('git commit --date="' + d + '" -m "commit"')

os.system('git push -u origin main')
#os.system('git config --global user.name "Prajakta Deokar"')
#os.system('git config --global user.email "prajaktadeokar1996@gmail.com"')

