# Task 4: Client configuration file (w/ Puppet) 
exec { 'turn off passwd auth",
  ensure  => '',
  path    => '/etc/ssh/ssh_config',
  command =>  'ssh_config IdentifyFile ~/.ssh/holberton PasswordAuthentication no',
}
