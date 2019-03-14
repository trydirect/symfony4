FROM php:7.2-fpm-alpine3.6
WORKDIR '/app'
RUN apk update && apk upgrade\
    && apk add --no-cache curl libbz2 php7-bz2 php7-pdo php7-pgsql php7-bcmath php7-zmq php7-curl bash php7-pear php7-imagick openssh\
    libtool \
    postgresql-dev \
    libpng-dev \
    imagemagick-c++ \
    imagemagick-dev \
    libmcrypt-dev \
    libxml2-dev \
    yaml-dev \
    bzip2 \
    aspell-dev \
    autoconf \
    build-base \
    linux-headers \
    libaio-dev \
    zlib-dev \
    git \
    subversion \
    freetype-dev \
    libjpeg-turbo-dev \
    libmcrypt-dev \
    bzip2-dev \
    libstdc++ \
    libxslt-dev \
    openldap-dev \
    hiredis-dev \
    make \
    unzip \
    ffmpeg \
    wget
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN docker-php-ext-install gd bcmath zip bz2 pdo pdo_pgsql simplexml opcache sockets mbstring pcntl xsl pspell
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/
RUN docker-php-ext-install pdo_mysql
RUN pecl install imagick
RUN docker-php-ext-enable imagick
RUN pecl install xdebug
RUN wget http://xdebug.org/files/xdebug-2.6.1.tgz
RUN tar -xvzf xdebug-2.6.1.tgz
RUN cd xdebug-2.6.1 \
    && phpize \
    && ./configure --enable-xdebug \
    && make \
    && make install \
    && cp modules/xdebug.so /usr/local/lib/php/extensions/no-debug-non-zts-20170718 \
    && echo 'zend_extension = /usr/local/lib/php/extensions/no-debug-non-zts-20170718/xdebug.so' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_enable=on' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_connect_back=1' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_host=127.0.0.1' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_port=9000' >> /usr/local/etc/php.ini \
    && echo 'xdebug.remote_handler=dbgp' >> /usr/local/etc/php.ini \
    && echo 'xdebug.max_nesting_level=512' >> /usr/local/etc/php.ini \
    && echo 'extension=xdebug.so' >> /usr/local/etc/php.ini
RUN cd /usr/src && curl -OL https://github.com/symfony/symfony/archive/v4.2.3.tar.gz
WORKDIR '/var/www/html'
