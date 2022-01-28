# Kubeflow pipelines middleware

docker build -t kfmdwimage .
docker run -d --name kfmdw -p 80:80 kfmdwimage:latest
