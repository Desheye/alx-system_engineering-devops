server {
    listen 80 default_server;
    listen [::]:80 default_server;
    add_header X-Served-By <%= @hostname %>;
    root   /var/www/html;
    index  index.html index.htm;

    location / {
        try_files $uri $uri/ =404;
    }
}
