# Exact copy of task 0 but done as puppet, each line of task 0 is within command
exec {'command':
    command => "sudo apt-get -y update && sudo apt-get -y install nginx && sudo sed -i \"42i \ add_header X-Served-By: $HOSTNAME;\" >> /etc/nginx/sites-available/default && sudo service nginx start",
    provider => shell,
}
