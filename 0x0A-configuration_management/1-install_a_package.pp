# Install Flask from pip3 using Puppet

package { 'python3-pip':
  ensure   => installed,
  provider => 'apt',
}

package { 'Flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip'],
}

package { 'Werkzeug':
  ensure   => '2.0.3',
  provider => 'pip3',
  require  => Package['Flask'],
}

