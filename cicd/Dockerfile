FROM python:3.11

RUN apt-get update && apt-get install -y git build-essential

WORKDIR /workspace

COPY cicd/requirements.txt /tmp/requirements.txt
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# 기본 JupyterLab 실행
CMD ["sh", "-c", "jupyter lab --ip=0.0.0.0 --port=8888 --allow-root --NotebookApp.token='' --NotebookApp.notebook_dir=/workspace"]