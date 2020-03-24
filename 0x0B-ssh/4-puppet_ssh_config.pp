# Task 4: Client configuration file (w/ Puppet) 
exec {
  command =>  'ssh_config IdentifyFile ~/.ssh/holberton PasswordAuthentication no',
}
