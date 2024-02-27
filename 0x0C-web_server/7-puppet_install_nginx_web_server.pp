# Setup New Ubuntu server with nginx

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
    ensure => 'installed',
    require => Exec['update system']
}

file {'/etc/nginx/sites-available/default':
    content => '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    location / {
        return 200 "Hello World!\n";
    }

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }
}
',
    require => Package['nginx']
}

file {'/var/www/html/index.html':
    content => 'Hello World!',
    require => Package['nginx']
}

service {'nginx':
    ensure => running,
    require => Package['nginx']
}
