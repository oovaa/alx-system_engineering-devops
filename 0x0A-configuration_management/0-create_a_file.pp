# Using Puppet, create a file in /tmp.
file { '/tmp/school':
  ensure  => 'file',      # Ensure it's a file
  mode    => '0744',      # Set file permissions
  owner   => 'www-data',  # Set file owner
  group   => 'www-data',  # Set file group
  content => 'I love Puppet',  # Set file content
}
