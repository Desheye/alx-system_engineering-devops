# Puppet manifest to fix the issue causing Apache to return a 500 error

exec { 'Replace .phpp file extension with .php in the specified file':
  command => "sed -i 's/class-wp-locale.phpp/class-wp-locale.php/g' /var/www/html/wp-settings.php",
  path    => '/bin'
}
