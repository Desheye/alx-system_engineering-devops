#!/usr/bin/env puppet

# Setup New Ubuntu server with nginx

exec { 'update system':
  command => '/usr/bin/apt-get update',
}

exec { 'install nginx':
  command => '/usr/bin/apt-get install -y nginx',
  require => Exec['update system'],
}

service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Exec['install nginx'],
}

file { '/var/www/html/index.nginx-debian.html':
  ensure  => file,
  content => "Hello World!\n",
  require => Service['nginx'],
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => template('nginx/default.erb'),
  require => File['/var/www/html/index.nginx-debian.html'],
}

file { '/var/www/html/error_404.html':
  ensure  => file,
  content => "Ceci n'est pas une page\n",
  require => Service['nginx'],
}

service { 'nginx':
  subscribe => File['/etc/nginx/sites-available/default'],
}

exec { 'allow nginx on firewall':
  command => '/usr/sbin/ufw allow 'Nginx HTTP'',
  require => Service['nginx'],
}

