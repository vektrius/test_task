docker build -t catalog .
docker rm -f catalog
docker run --name catalog -v ./:/app -p 8000:8000 catalog
