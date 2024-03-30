# Add a custom HTTP header and setup a new Ubuntu server with nginx

exec { 'HTTP header':
	command => '/usr/bin/sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec { 'redirect_me':
	command => '/usr/bin/sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

file { '/var/www/html/index.html':
	content => 'Hello World!'
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

service { 'nginx':
	ensure => running,
	require => Package['nginx']
}

