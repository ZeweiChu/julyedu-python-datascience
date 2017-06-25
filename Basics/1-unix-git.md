# 命令行和Git入门
## 命令行基础
切换路径
```
cd [your path]
```

新建文件夹
```
mkdir [dir name]
```

显示当前路径下的文件和文件夹
```
ls
```

显示当前路径
```
pwd
```

回到上一级目录
```
cd ..
```

回到home目录
```
cd ~
```

删除文件
```
rm [file name]
```

重命名文件/文件夹
```
mv [file name] [new file name]
```


## Git基础

To initialize a directory as a working directory
把一个文件夹初始化成一个git的工作文件夹
```bash
git init
```
It creates a direcotry .git to track your project

To check status of current local directory
查看当前git文件夹的状态
```bash
git status
```

To add some file to the staging area
把文件加到展示台上
```
git add <filename>
```


remove all files from the staging area, to make them untracked files
把所有的文件移下展示台
```
git reset
```


commit files from staging area to the local git repository
把文件从展示台上传到本地git repository
```
git commit -m "some commit information"
```




clone a remote repository to local
克隆远程repository
```
git clone <url> <where to clone>
```

list information of the remote repository
```
git remote -v
```


list all branches locally and remotely
```
git branch -a
```


push a local repository to remote master repository
```
git push origin master
```

pull from remote repository to local repository
```
git pull
```


### Common workflow
```
git branch <name-of-branch>
git branch
git checkout <name-of-branch>
git branch
```
make changes to the branch
```
git status
git add -A
git commit -m "adding some function"
git push -u origin <name-of-branch>
```


