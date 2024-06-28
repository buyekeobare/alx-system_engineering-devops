# Install flask from pip3 using puppet
exec {'Install flask using pip3':
  command => '/usr/bin/pip3 install flask==2.1.0',
}
