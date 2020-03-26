# Task 4: Client configuration file (w/ Puppet) 
include stdlib
file_line { 'turn off passwd auth':
  ensure  =>  present,
  path    =>  '/etc/ssh/ssh_config',
  line    =>  'PasswordAuthentication no',
;
'declare identity file':
  ensure  =>  present,
  path    =>  '/etc/ssh/ssh_config'
  line    =>  'IdentifyFile ~/.ssh/holberton'
}
