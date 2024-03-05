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

# add custom header to nginx configuration
file_line { 'nginx_custom_header':
  path    => '/etc/nginx/sites-available/default',
  line    => '    add_header X-Served-By $hostname;',
  match   => '^    location / {$',
  after   => '^    location / {$',
  require => Package['nginx'],
  notify  => Service['nginx'],
}

service { 'nginx':
  ensure => running,
  enable => true,
}