[![Build Status](https://travis-ci.com/trydirect/symfony.svg?branch=master)](https://travis-ci.com/trydirect/symfony)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/symfony.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/symfony.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/symfony.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/symfony.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/trydirect/community)

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





## Contributing

1. Fork it (<https://github.com/trydirect/symfony4/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
