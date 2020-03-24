# Task 2: Execute a command
exec {
  path    =>  '/usr/bin',
  command =>  'pkill -f ./killmenow',
}
