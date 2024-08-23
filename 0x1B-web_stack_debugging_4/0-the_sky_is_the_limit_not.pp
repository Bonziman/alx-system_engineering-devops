# Increases the amount of traffic an Nginx server can handle.

# Increase the ULIMIT of the default file
exec { 'fix_for_nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => ['/usr/local/bin', '/bin'],
  unless  => 'grep -q "4096" /etc/default/nginx',
}

# Restart Nginx
exec { 'nginx_restart':
  command => '/etc/init.d/nginx restart',
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  require => Exec['fix_for_nginx'],
}
