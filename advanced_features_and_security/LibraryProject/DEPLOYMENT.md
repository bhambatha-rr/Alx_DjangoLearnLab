# Deployment Configuration for HTTPS

This document outlines the necessary web server configuration to support the HTTPS settings enabled in this Django project. The following is a sample configuration for **Nginx**.

## Prerequisites

1.  A domain name (e.g., `yourdomain.com`).
2.  An SSL/TLS certificate for your domain. This can be obtained for free from [Let's Encrypt](https://letsencrypt.org/) using Certbot.

## Sample Nginx Configuration

This configuration listens on port 80 (HTTP) and permanently redirects all traffic to port 443 (HTTPS). The HTTPS server block then handles the SSL/TLS termination and proxies requests to the Django application running on a local port (e.g., 8000).

```nginx
# /etc/nginx/sites-available/yourproject

# Server block to redirect HTTP to HTTPS
server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    return 301 https://$server_name$request_uri;
}

# Main server block for HTTPS
server {
    listen 443 ssl;
    server_name yourdomain.com www.yourdomain.com;

    # SSL Certificate paths (provided by Certbot or your SSL provider)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    # SSL/TLS security enhancements
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'TLS_AES_128_GCM_SHA256:TLS_AES_256_GCM_SHA384:ECDHE-RSA-AES128-GCM-SHA256';
    ssl_prefer_server_ciphers off;

    # Add the HSTS header (Django also does this, but it's good practice here too)
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;

    location / {
        # Proxy requests to the Django application server (e.g., Gunicorn)
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location /static/ {
        alias /path/to/your/project/static/;
    }

    location /media/ {
        alias /path/to/your/project/media/;
    }
}
