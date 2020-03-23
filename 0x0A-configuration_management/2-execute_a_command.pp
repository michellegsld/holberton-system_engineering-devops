# Task 2: Execute a command
exec {
  command =>  'if pgrep killmenow; then pkill -f ./killmenow; fi',
}
