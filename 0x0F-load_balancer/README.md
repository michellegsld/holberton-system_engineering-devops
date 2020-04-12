### README for 0x0F-load_balancer ###
#### A directory within the holberton-system_engineering-devops repo ####

| File Name | Description |
| --------- | ----------- |
| 0-custom_http_response-header | Configure `web-02` to be identical to `web-01`, and configure Nginx so that it's HTTP response contains a custom header on both web servers. |
| 1-install_load_balancer | Install and configure HAproxy with version equal or greater than 1.5 on your `lb-01` server, so that sends traffic to `web-01` and `web-02`. |
| 2-puppet_custom_http_response-header.pp | Does exactly the same as `0-custom_http_response-header`, but uses puppet to complete it instead. |
