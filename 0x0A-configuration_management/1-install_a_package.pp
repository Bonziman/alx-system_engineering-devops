# install flask from pip3
package { 'pip3':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0',
  unless  => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
  require => Package['pip3'],
}
