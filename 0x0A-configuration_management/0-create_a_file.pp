# Task 0: Create a file
file { '/tmp/holberton':
  ensure  =>  'file',
  path    =>  '/tmp/holberton',
  content =>  'I love Puppet',
  mode    =>  '0744',
  group   =>  'www-data',
  owner   =>  'www-data',
}
