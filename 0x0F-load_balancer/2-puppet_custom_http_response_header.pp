# execute 'apt-get update'
exec { 'apt-update':
  command => '/usr/bin/apt update'
}

# install nginx package
package { 'nginx':
  require => Exec['apt-update'],
  ensure  => installed,
}

file { '/var/www/html/index.html':
  ensure  => file,
  content => 'Hello World!',
  require => Package['nginx']
}

file { '/etc/nginx/sites-available/default':
  ensure  => file,
  content => template('nginx/default.erb'),
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}