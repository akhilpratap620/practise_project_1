# practise_project_1
This is first actual project
conda creating venv
```
conda creat -p <enviroment_name> python==3.7 -y
```
```
conda activate venv/
```
```
Requirement.txt will be created
``` 

```
pip install -r requirements.txt
```
to add file in git 
```
git add . 
```
to chech status
```
git status
```
to commit
```
git commit -m "<message>"
```
to push code on git 
```
git push origin main
```
Note:>to ignore file or folder we use name of file .gitignore file
to check remote url 
```
git remote -v
```
To setup cicd pipeline in heroku we need three information
1. HEROKU_EMAIL =akhilfan12345@gmail.com
2. HEROKU_API_KEY= d722ca4d-dcbb-40aa-a30e-53c69ef2344b
3. HEROKU_APP_NAME= akhilregress
docker build image
```
docker build -t <image_name>:<tag_name> .
```
to list docker images
```
docker images
```
to run docker image 
```
docker run -p 5000:5000 -e PORT=5000 <image_id>
to check any running container
``` docker ps
```
to stop docker container
```docker stop <container_id >
```

