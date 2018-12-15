## Install Docker

```

$ sudo apt-get update && sudo apt-get upgrade -y
$ sudo apt-get install -y linux-image-extra-$(uname -r) linux-image-extra-virtual
$ sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
$ sudo apt-get update
$ sudo apt-get install -y docker-ce
$ sudo usermod -aG docker $USER

```

## Install Docker-Compose

```

$ sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose

```

## Run APP

1. Deploy

```

$ docker-compose build

```

2. Run

```

$ docker-compose up -d

```

3. Init DB

```

$ docker exec -it web bash
$ python manage.py db init
$ python manage.py db migrate
$ python manage.py db upgrade
$ exit

```

