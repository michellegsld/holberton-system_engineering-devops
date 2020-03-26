# Task 4: Client configuration file (w/ Puppet) 
include stdlib
file_line {
  'Turn off passwd auth':
  ensure =>  present,
  path   =>  '/etc/ssh/ssh_config',
  line   =>  'PasswordAuthentication no',
;
'Declare identity file':
  ensure =>  present,
  path   =>  '/etc/ssh/ssh_config'
  line   =>  'IdentifyFile ~/.ssh/holberton'
}
