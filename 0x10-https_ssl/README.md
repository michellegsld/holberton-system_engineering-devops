### README for 0x10-https_ssl ###
#### A directory within the holberton-system_engineering-devops repo ####

| File Name | Description |
| --------- | ----------- |
| 0-https_abc | Contains answers to these multiple choice questions:<br>What is HTTPS?<br>&nbsp;&nbsp;&nbsp;1. A secure version of HTTP<br>&nbsp;&nbsp;&nbsp;2. A faster version of HTTP<br>&nbsp;&nbsp;&nbsp;3. A superior version of HTTP<br>Why do you need HTTPS?<br>&nbsp;&nbsp;&nbsp;1. To encrypt credit card and social security number information going between the client and the website servers<br>&nbsp;&nbsp;&nbsp;2. To encrypt all communication between the client and the website servers<br>&nbsp;&nbsp;&nbsp;3. To accelerate the communication between the client and the website servers<br>You want to setup HTTPS on your website, where shall you place the certificate?<br>&nbsp;&nbsp;&nbsp;1. In a secure location where nobody can access it<br>&nbsp;&nbsp;&nbsp;2. You can host it anywhere but you have to share the link to it on your website<br>&nbsp;&nbsp;&nbsp;3. On your website web server(s) |
| 1-world_wide_web | Configure your domain zone so that the subdomain `www` points to your load-balancer IP (`lb-01`). Also add other subdomains and use a Bash script in order to display the information about those subdomains. |
| 2-haproxy_ssl_termination | Create a certificate using `certbot` and configure `HAproxy` to accept encrypted traffic for your subdomain `www.`. |
| 100-redirect_http_to_https | HAproxy configuration to enforce HTTPS traffic so that no unencrypted traffic is possible by automatically redirecting HTTP traffic to HTTPS. |
