# Task 0: Create a file
file { '/tmp/holberton.pp':
  ensure  =>  'file',
  content =>  'I love Puppet',
  mode    =>  '0744',
  group   =>  'www-data',
  owner   =>  'www-data',
}
