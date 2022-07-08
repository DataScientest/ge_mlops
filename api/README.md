# MLOps

## To run locally

```sh
cd api
python3 -m venv venv

source venv/bin/activate
pip3 install -r requirements.txt

python3 -m uvicorn main:api --host=0.0.0.0

```

## To build the Docker image

To perform this step, you need to have Docker Engine installed and running. You can use the virtual machine available on the platform.

```sh
cd api
docker build . -t my_image
```

## To run the Docker image

```sh
docker container run -p 8000:8000 my_image
# or if you want to use the image built during the masterclass
docker container run -p 8000:8000