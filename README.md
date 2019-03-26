# symfony 4
 Symfony4 template with:
 * docker-compose
 * php-fpm 7.2
 * Xdebug 2.6.1
 * Nginx
 * Supervisord
 * mysql 5.7
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
