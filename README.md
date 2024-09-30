# IOT Raspberry Pi Proxy

Using Nginx running inside Docker, run with docker compose

## Install Docker and docker-compose

```
sudo apt-get update
sudo apt-get upgrade -y
curl -sSL https://get.docker.com | sh
sudo usermod -aG docker $USER
sudo curl -L https://github.com/docker/compose/releases/download/v2.29.7/docker-compose-`uname -s`-`uname -m` > docker-compose
sudo mv docker-compose /usr/bin/
sudo chown root: /usr/bin/docker-compose
sudo chmod +x /usr/bin/docker-compose
```

## Set Docker to run on startup

```
sudo systemctl enable docker
```

## Updating Nginx configuration with new service to `default.conf`:

```
location /newservice {
    proxy_pass http://192.168.1.130:8080/;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}
```
ensure you are pointing to the right domain:
```
server_name iot.vaughndv.com;  # Replace with your domain name
```


## Run proxy

```
docker-compose up -d
```

## Debugging

```
docker-compose logs
```


