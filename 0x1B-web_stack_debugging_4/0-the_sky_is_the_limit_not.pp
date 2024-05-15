# Update Nginx settings to accommodate higher request volumes
exec { 'adjusting Nginx settings':
  # Modify the ulimit value
  command => '/bin/sed -i "s/15/4096/" /etc/default/nginx',
  # Specify the path for the sed command
  path    => '/usr/local/bin:/bin',
}

exec { 'restart Nginx service':
  # Restart Nginx service
  command => '/etc/init.d/nginx restart',
  # Specify the path for the service restart command
  path    => '/etc/init.d/',
}
