# install_flask
exec { 'install_flask':
  command     => '/usr/bin/pip3 install Flask==2.1.0',
  path        => '/usr/bin',
  refreshonly => true,
}

