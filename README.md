[![Build Status](https://travis-ci.com/trydirect/symfony4.svg?branch=master)](https://travis-ci.com/trydirect/symfony4)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/symfony.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/symfony.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/symfony.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/symfony.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)

# Symfony 4
 Symfony 4 template includes:
 * PHP-fpm 7.2
 * MySQL 5.7
 * Xdebug 2.6.1
 * Nginx
 * Supervisord
 * docker-compose
 * Ubuntu 18.04
 
This repo help Symfony developers to start their new projects quickly using docker-compose.
Docker image includes Xdebug.

## Note
Before installing this project, please, make sure you have installed docker and docker-compose

To install docker execute: 
```sh
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
$ pip install docker-compose
```

## Installation
Clone this project into your work directory:
```sh
$ git clone "https://github.com/trydirect/symfony4.git"
```
Then build it via docker-compose:
```sh
$ cd symfony4
$ docker-compose up -d
```


## Quick deployment to cloud
##### Amazon AWS, Digital Ocean, Hetzner and others
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://try.direct/server/user/deploy/InN5bWZvbnk0fDZ8MTki.EAoFeA.Uld1w-ATQ9xrFu2TE71thWuSnag/)



## Let's check the deployment result in browser
 

| **Url** | **App** |
| --- | --- |
| http://localhost       | Symfony home page       |
| http://localhost:5601  | Kibana                  |
| http://localhost:9200  | Elasticsearch           |



## Run Tests

```
$ python tests.py 
```

## Contributing

1. Fork it (<https://github.com/trydirect/symfony4/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request

# Support Development

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL)
